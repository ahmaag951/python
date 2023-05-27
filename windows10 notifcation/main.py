from win10toast import ToastNotifier

toast = ToastNotifier()

toast.show_toast(
    # "Notification from Ahmed Ezzat",
    "HOZAIFA",
    "This is a notification made by the great python language",
    # duration = 10,
    icon_path = "python.ico",
    threaded = True,
)
