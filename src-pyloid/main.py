from pyloid import Pyloid, PyloidAPI, Bridge, TrayEvent, is_production, get_production_path
import os

app = Pyloid(app_name="Pyloid-App", single_instance=True)

# set icon
if (is_production()):
    app.set_icon(os.path.join(get_production_path(), "icons/icon.png"))
else:
    app.set_icon("src-pyloid/icons/icon.png")

# set tray
app.set_tray_actions(
    {
        TrayEvent.DoubleClick: lambda: print("Tray icon double-clicked."),
    }
)
app.set_tray_menu_items(
    [
        {"label": "Show Window", "callback": lambda: app.show_and_focus_main_window()},
        {"label": "Quit", "callback": lambda: app.quit()},
    ]
)
app.run_tray()

# set custom api
class CustomAPI(PyloidAPI):
    @Bridge(result=str)
    def create_window(self):
        window = app.create_window(
            title="Pyloid Alert",
            frame=False,
            context_menu=False,
            js_apis=[CustomAPI()],
            dev_tools=True
        )

        window.set_size(400, 200)

        # set position to right bottom
        monitor = app.get_primary_monitor()
        available_size = monitor.available_size()
        window.set_position(available_size['width'] - window.width, available_size['height'] - window.height)

        # load html
        if (is_production()):
            window.load_file(os.path.join(get_production_path(), "src/alert.html"))
        else:
            window.load_file("src/alert.html")
        window.show()
        window.focus()

        return window.id

# create window
window = app.create_window(
    title="Pyloid Browser1",
    js_apis=[CustomAPI()],
    dev_tools=True
)

window.set_size(800, 600)

# load html
if (is_production()):
    window.set_dev_tools(False)
    window.load_file(os.path.join(get_production_path(), "src/index.html"))
else:
    window.load_file("src/index.html")

# show window
window.show_and_focus()

app.run()
