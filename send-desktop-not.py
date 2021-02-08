from win10toast import ToastNotifier

# Inicializa #
toaster = ToastNotifier()

# Passa parâmetros e mostra a notificação #
toaster.show_toast(
    "Notificação", 
    "Olá Pycodebr :)", 
    threaded=True, 
    icon_path=None, 
    duration=3 # 3 segundos
)