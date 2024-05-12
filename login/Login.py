from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel




class ConfigScreen(MDScreen):
    def __init__(self, **kwargs):
        super(ConfigScreen, self).__init__(**kwargs)

        # Criando uma lista de configurações com descrições
        config_list = [
            ("Segurança", "security", "Configurações de segurança do aplicativo"),
            ("Visibilidade", "eye", "Opções de visibilidade"),
            ("Privacidade de Dados", "lock", "Controle de privacidade e segurança de dados"),
            ("Notificações", "bell-ring", "Gerencie as notificações do aplicativo"),
            ("Logout", "logout", "Sair da conta e fazer logout do aplicativo")
        ]

        # Adicionando o ícone do usuário e itens de configuração à tela
        scroll_view = ScrollView()
        main_layout = BoxLayout(orientation="vertical")

        # Adicionando layout do usuário
        user_layout = BoxLayout(orientation="horizontal", padding="10dp", size_hint_y=None, height="72dp")
        user_icon = IconLeftWidget(icon="account-circle", theme_text_color="Primary", size=("48dp", "48dp"))
        user_label = MDLabel(text="Usuário", halign="left", font_style="H6", size_hint_x=None, width="120dp")
        user_layout.add_widget(user_icon)
        user_layout.add_widget(user_label)
        main_layout.add_widget(user_layout)

        # Adicionando separador
        main_layout.add_widget(MDLabel(size_hint_y=None, height="1dp"))

        # Adicionando configurações
        config_layout = self.create_config_layout(config_list)
        scroll_view.add_widget(config_layout)
        main_layout.add_widget(scroll_view)
        self.add_widget(main_layout)

    def create_config_layout(self, config_list):
        config_layout = BoxLayout(orientation="vertical")
        for config_option, icon_name, description in config_list:
            item = ThreeLineIconListItem(text=config_option, secondary_text="", tertiary_text=description)
            icon = IconLeftWidget(icon=icon_name)
            item.add_widget(icon)
            config_layout.add_widget(item)
        return config_layout


class ConfiguraçõesApp(MDApp):
    def build(self):
        return ConfigScreen()


if __name__ == "__main__":
    ConfiguraçõesApp().run()
