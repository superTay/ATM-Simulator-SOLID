import tkinter as tk
from tkinter import messagebox

# Importar tu lógica existente
from accounts.factory import AccountFactory
from cards.debit_card import DebitCard
from cards.credit_card import CreditCard


class Session:
    """Mantiene el estado de la sesión actual de ATM."""
    def __init__(self):
        self.card = None
        self.account = None
        self.authenticated = False

    def reset(self):
        self.card = None
        self.account = None
        self.authenticated = False


class ATMApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ATM - Simulador")
        self.geometry("420x560")
        self.resizable(False, False)

        # Datos de ejemplo: crear cuentas y tarjetas usando tu modelo
        self._seed_demo_data()

        self.session = Session()

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (WelcomeScreen, CardInsertScreen, PinScreen, MenuScreen, AmountScreen, ReceiptScreen):
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomeScreen")

    def _seed_demo_data(self):
        # Crear cuentas de ejemplo con la factory si existe
        # Crear una factory; si tu AccountFactory requiere un manager concreto,
        # asume su propia configuración interna.
        factory = AccountFactory()
        # Cuentas
        # Ajustar a las firmas reales de tus cuentas
        # Checking/Savings: (account_holder: str, account_number: str, balance: float = 0.0)
        checking = factory.create_account(
            "checking",
            account_holder="Alice",
            account_number="CHK-001",
            balance=1000.0,
        )
        savings = factory.create_account(
            "savings",
            account_holder="Bob",
            account_number="SAV-001",
            balance=2500.0,
        )
        # Credit: (account_holder: str, account_number: str, credit_limit: float, interest_rate: float, balance: float = 0.0)
        credit = factory.create_account(
            "credit",
            account_holder="Carlos",
            account_number="CRD-001",
            credit_limit=1500.0,
            interest_rate=20.0,
            balance=0.0,
        )

        # Tarjetas asociadas
        self.demo_cards = [
            DebitCard(card_number="1111222233334444", pin="1234", linked_account=checking),
            DebitCard(card_number="5555666677778888", pin="4321", linked_account=savings),
            CreditCard(card_number="9999000011112222", pin="2468", linked_account=credit),
        ]

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def get_card_by_last4(self, last4: str):
        for c in self.demo_cards:
            if c._card_number.endswith(last4):
                return c
        return None


class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller: ATMApp):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Bienvenido/a", font=("Arial", 22, "bold")).pack(pady=30)
        tk.Label(self, text="Inserte su tarjeta para comenzar", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Insertar tarjeta", font=("Arial", 16), width=20,
                  command=lambda: controller.show_frame("CardInsertScreen")).pack(pady=40)


class CardInsertScreen(tk.Frame):
    def __init__(self, parent, controller: ATMApp):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Identificación de tarjeta", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(self, text="Ingrese los 4 últimos dígitos", font=("Arial", 14)).pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 18), justify="center")
        self.entry.pack(pady=10)

        btns = tk.Frame(self)
        btns.pack(pady=10)
        tk.Button(btns, text="Continuar", font=("Arial", 14), width=12, command=self.continue_next).grid(row=0, column=0, padx=6)
        tk.Button(btns, text="Volver", font=("Arial", 14), width=12, command=lambda: controller.show_frame("WelcomeScreen")).grid(row=0, column=1, padx=6)

        # Ayuda: listar tarjetas demo
        tk.Label(self, text="Tarjetas demo: 4444, 8888, 2222", font=("Arial", 10), fg="#555").pack(pady=6)

    def continue_next(self):
        last4 = self.entry.get().strip()
        card = self.controller.get_card_by_last4(last4)
        if not card:
            messagebox.showerror("Tarjeta", "No se encontró una tarjeta con esos dígitos.")
            return
        self.controller.session.card = card
        self.controller.show_frame("PinScreen")


class PinScreen(tk.Frame):
    def __init__(self, parent, controller: ATMApp):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Ingrese su PIN", font=("Arial", 20, "bold")).pack(pady=20)

        self.pin_var = tk.StringVar()
        self.display = tk.Entry(self, font=("Arial", 22), textvariable=self.pin_var, justify="center", show="•", width=10)
        self.display.pack(pady=10)

        keypad = tk.Frame(self)
        keypad.pack(pady=10)
        buttons = [
            '1','2','3',
            '4','5','6',
            '7','8','9',
            '←','0','OK'
        ]
        for i, b in enumerate(buttons):
            cmd = (lambda x=b: self.on_key(x))
            tk.Button(keypad, text=b, font=("Arial", 18), width=5, height=2, command=cmd).grid(row=i//3, column=i%3, padx=6, pady=6)

        tk.Button(self, text="Cancelar", font=("Arial", 14), command=self.cancel).pack(pady=6)

    def on_key(self, key):
        if key == 'OK':
            self._validate()
        elif key == '←':
            current = self.pin_var.get()
            self.pin_var.set(current[:-1])
        else:
            if len(self.pin_var.get()) < 6:
                self.pin_var.set(self.pin_var.get() + key)

    def _validate(self):
        pin = self.pin_var.get()
        card = self.controller.session.card
        if not card:
            messagebox.showerror("Error", "No hay tarjeta seleccionada.")
            return
        if card.validate_pin(pin):
            self.controller.session.authenticated = True
            self.controller.session.account = card.get_account()
            self.pin_var.set("")
            self.controller.show_frame("MenuScreen")
        else:
            messagebox.showerror("PIN", "PIN incorrecto. Intente de nuevo.")
            self.pin_var.set("")

    def cancel(self):
        self.controller.session.reset()
        self.pin_var.set("")
        self.controller.show_frame("WelcomeScreen")


class MenuScreen(tk.Frame):
    def __init__(self, parent, controller: ATMApp):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Seleccione una opción", font=("Arial", 20, "bold")).pack(pady=20)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Ver saldo", font=("Arial", 16), width=16, command=self.show_balance).grid(row=0, column=0, padx=8, pady=8)
        tk.Button(btn_frame, text="Retirar", font=("Arial", 16), width=16, command=lambda: self.goto_amount('withdraw')).grid(row=0, column=1, padx=8, pady=8)
        tk.Button(btn_frame, text="Depositar", font=("Arial", 16), width=16, command=lambda: self.goto_amount('deposit')).grid(row=1, column=0, padx=8, pady=8)
        tk.Button(btn_frame, text="Salir", font=("Arial", 16), width=16, command=self.exit_session).grid(row=1, column=1, padx=8, pady=8)

    def _require_session(self):
        if not (self.controller.session.authenticated and self.controller.session.account):
            messagebox.showerror("Sesión", "Sesión no válida. Regresando al inicio.")
            self.controller.session.reset()
            self.controller.show_frame("WelcomeScreen")
            return False
        return True

    def show_balance(self):
        if not self._require_session():
            return
        acc = self.controller.session.account
        try:
            balance = acc.get_balance()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener el saldo: {e}")
            return
        self.controller.frames["ReceiptScreen"].set_message(f"Saldo disponible: ${balance:.2f}")
        self.controller.show_frame("ReceiptScreen")

    def goto_amount(self, op):
        if not self._require_session():
            return
        amount_screen = self.controller.frames["AmountScreen"]
        amount_screen.set_mode(op)
        self.controller.show_frame("AmountScreen")

    def exit_session(self):
        self.controller.session.reset()
        self.controller.show_frame("WelcomeScreen")


class AmountScreen(tk.Frame):
    def __init__(self, parent, controller: ATMApp):
        super().__init__(parent)
        self.controller = controller
        self.mode = None  # 'withdraw' o 'deposit'

        self.title_lbl = tk.Label(self, text="", font=("Arial", 20, "bold"))
        self.title_lbl.pack(pady=16)

        self.amount_var = tk.StringVar()
        self.display = tk.Entry(self, font=("Arial", 22), textvariable=self.amount_var, justify="center", width=12)
        self.display.pack(pady=10)

        keypad = tk.Frame(self)
        keypad.pack(pady=8)
        buttons = [
            '1','2','3',
            '4','5','6',
            '7','8','9',
            '←','0','OK'
        ]
        for i, b in enumerate(buttons):
            cmd = (lambda x=b: self.on_key(x))
            tk.Button(keypad, text=b, font=("Arial", 18), width=5, height=2, command=cmd).grid(row=i//3, column=i%3, padx=6, pady=6)

        tk.Button(self, text="Cancelar", font=("Arial", 14), command=lambda: controller.show_frame("MenuScreen")).pack(pady=6)

    def set_mode(self, mode: str):
        self.mode = mode
        self.amount_var.set("")
        if mode == 'withdraw':
            self.title_lbl.config(text="Ingrese monto a retirar")
        else:
            self.title_lbl.config(text="Ingrese monto a depositar")

    def on_key(self, key):
        if key == 'OK':
            self._confirm()
        elif key == '←':
            self.amount_var.set(self.amount_var.get()[:-1])
        else:
            # Solo números y un único punto decimal
            if key.isdigit():
                self.amount_var.set(self.amount_var.get() + key)

    def _confirm(self):
        txt = self.amount_var.get().strip()
        if not txt:
            messagebox.showwarning("Monto", "Ingrese un monto válido.")
            return
        try:
            amount = float(txt)
        except ValueError:
            messagebox.showerror("Monto", "Formato de monto inválido.")
            return
        if amount <= 0:
            messagebox.showerror("Monto", "El monto debe ser mayor que 0.")
            return

        acc = self.controller.session.account
        result_msg = ""
        try:
            if self.mode == 'withdraw':
                acc.withdraw(amount)
                result_msg = f"Retiro exitoso: ${amount:.2f}. Saldo: ${acc.get_balance():.2f}"
            else:
                acc.deposit(amount)
                result_msg = f"Depósito exitoso: ${amount:.2f}. Saldo: ${acc.get_balance():.2f}"
        except Exception as e:
            messagebox.showerror("Operación", f"No se pudo completar: {e}")
            return

        self.controller.frames["ReceiptScreen"].set_message(result_msg)
        self.controller.show_frame("ReceiptScreen")


class ReceiptScreen(tk.Frame):
    def __init__(self, parent, controller: ATMApp):
        super().__init__(parent)
        self.controller = controller
        self.msg_var = tk.StringVar(value="")
        tk.Label(self, textvariable=self.msg_var, font=("Arial", 16), wraplength=380, justify="center").pack(pady=40)
        tk.Button(self, text="Volver al menú", font=("Arial", 14), command=lambda: controller.show_frame("MenuScreen")).pack(pady=10)
        tk.Button(self, text="Finalizar", font=("Arial", 14), command=self.end_session).pack(pady=6)

    def set_message(self, msg: str):
        self.msg_var.set(msg)

    def end_session(self):
        self.controller.session.reset()
        self.controller.show_frame("WelcomeScreen")


def main():
    app = ATMApp()
    app.mainloop()


if __name__ == "__main__":
    main()
