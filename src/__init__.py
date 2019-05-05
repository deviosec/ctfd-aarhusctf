from CTFd.utils.plugins import register_script, register_stylesheet
from CTFd.plugins import register_plugin_assets_directory
import os

class ctfdaarhusctf(object):
    def __init__(self, app):
        # get our app handle
        self.app = app

        # find our plugin path!
        self.fullPath = os.path.dirname(os.path.realpath(__file__))+"/"
        # get our plugin path name (/plugins/octp/)
        pluginPath = os.path.dirname(__file__)
        splitPluginPath = pluginPath.split("/")
        self.partialPath = "/"+splitPluginPath[-2:][0]+"/"+splitPluginPath[-1:][0]+"/"


        # register our assets
        register_plugin_assets_directory(app, base_path=self.partialPath+"assets/")
        register_stylesheet(self.partialPath+"assets/style.css")

def load(app):
    x = ctfdaarhusctf(app)
    # create our table
    app.db.create_all()
