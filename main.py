from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import fonts

KV = '''
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts

# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.who_is
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: app.title 
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                        md_bg_color: 0, 0, 0, 1
                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1
                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] Input"

                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"   

                                BoxLayout:
                                    orientation: 'horizontal'                               

                                    MDIconButton:
                                        icon: "calendar-month"

                                    MDTextField:
                                        id: start_date
                                        hint_text: "Start date"
                                        on_focus: if self.focus: app.date_dialog.open()                                        
                                        color_mode: 'custom' 
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        text_hint_color: 0,0,1,1                                 

                                BoxLayout:
                                    orientation: 'horizontal'                         

                                    MDIconButton:
                                        icon: "cash"

                                    MDTextField:
                                        id: loan
                                        hint_text: "Loan"
                                        color_mode: 'custom' 
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1

                                BoxLayout:
                                    orientation: 'horizontal'                                

                                    MDIconButton:
                                        icon: "clock-time-five-outline"

                                    MDTextField:
                                        id: months
                                        hint_text: "Months"                                        
                                        color_mode: 'custom' 
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1


                                BoxLayout:
                                    orientation: 'horizontal'                                 

                                    MDIconButton:
                                        icon: "bank"

                                    MDTextField:
                                        id: interest
                                        hint_text: "Interest, %"
                                        color_mode: 'custom' 
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1

                                    MDTextField:
                                        id: payment_type
                                        hint_text: "Payment type"
                                        on_focus: if self.focus: app.menu.open()
                                        color_mode: 'custom' 
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1

                                MDSeparator:
                                    height: "1dp"

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: "Payment"

                                    MDTextField:
                                        id: payment_label
                                        hint_text: ""
                                        disabled: True

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: "Total interest"

                                    MDTextField:
                                        id: overpayment_loan_label
                                        hint_text: ""
                                        disabled: True

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: "Total payments"

                                    MDTextField:
                                        id: total_amount_of_payments_label
                                        hint_text: ""
                                        disabled: True

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: "Effective %"

                                    MDTextField:
                                        id: effective_interest_rate_label
                                        hint_text: ""
                                        disabled: True
                                        text_hint_color:[0,0,1,1]


                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] Table"

                            ScrollView:

                                BoxLayout:
                                    orientation: 'vertical'
                                    id: calc_data_table

                            MDFloatingActionButton:
                                icon: "email-outline"
                                pos: 20, 20
                                on_release: app.show_confirmation_dialog()

                        Tab:
                            id: tab3
                            name: 'tab3'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/size][/font] Graph"

                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"


                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: "10dp"
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50

                                    canvas:
                                        Color:
                                            rgba: 0.2, 0.2, 0.2, 0.1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos

                                    MDLabel:
                                        text: "Payment"
                                        halign: "center"
                                        font_style: "H5"
                                        height: "48dp"

                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: "10dp"
                                    id: graph

                                    canvas:
                                        Color:
                                            rgba: 1, 1, 1, 1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos   

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50  

                                    MDIcon:
                                        icon: "checkbox-blank"
                                        halign: "right"
                                        color: 0, 0, 1, 1

                                    MDLabel:
                                        text: "Interest"
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"

                                    MDIcon:
                                        icon: "checkbox-blank"
                                        halign: "right"
                                        color: 1, 0, 0, 1

                                    MDLabel:
                                        text: "Principal"
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"

                        Tab:
                            id: tab4
                            name: 'tab4'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] Chart"

                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"


                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: "10dp"
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50

                                    canvas:
                                        Color:
                                            rgba: 0.2, 0.2, 0.2, 0.1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos

                                    MDLabel:
                                        text: "Total payments"
                                        halign: "center"
                                        font_style: "H5"
                                        height: "48dp"

                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: "10dp"
                                    id: chart

                                    canvas:
                                        Color:
                                            rgba: 1, 1, 1, .6
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50  

                                    MDIcon:
                                        icon: "checkbox-blank"
                                        halign: "right"
                                        color: 0, 0, 1, 1

                                    MDLabel:
                                        text: "Interest"
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"

                                    MDIcon:
                                        icon: "checkbox-blank"
                                        halign: "right"
                                        color: 1, 0, 0, 1

                                    MDLabel:
                                        text: "Principal"
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"



                        Tab:
                            id: tab5
                            name: 'tab5'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['book-open-variant']}[/size][/font] Sum"



        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class Tab(MDFloatLayout, MDTabsBase):
    pass


class KopitinBro(MDApp):
    title = "Kopitin Bro"
    who_is = "Kopitin Boss"

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        icons_item_menu_lines = {
            "account-cowboy-hat": "О Димане",
            "account-multiple": "О его друзьях",
            "coffee": "О его увлечениях",
            }
        icons_item_menu_tabs = {
            "table-large": "Table",
            "chart-pie": "Chart"
        }
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )
#        for name_tab in list(md_icons.keys())[15:30]:
#            self.root.ids.tabs.add_widget(Tab(icon=name_tab, title=name_tab))
#        for icon_name, name_tab in icons_item_menu_tabs.items():
#            self.root.ids.tabs.add_widget(Tab(text=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/font][/ref] {name_tab}"))

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''
        Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
        # get the tab icon.
        count_icon = instance_tab.icon
        # print it on shell/bash.
        print(f"Welcome to {count_icon}' tab'" + tab_text)



    def share_it(self, *args):
        share("title_share", "this content to share!")
    def on_star_click(self):
        print("star clicked!")


KopitinBro().run()