#pip install kivy
#pip install kivymd
#pip install https://github.com/kivymd/KivyMD/archive/3274d62.zip

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import fonts
from kivymd.uix.picker import MDDatePicker
import datetime
import calendar

from kivy.graphics import Color, Rectangle, Line, Ellipse
from random import random as r
from kivy.uix.floatlayout import FloatLayout


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
                                    
                                MDIconButton:
                                    icon: "language-python"
                                    pos_hint: {"center_x": .5, "center_y": .5}
                                    on_release: app.calc_table(*args)
                                    on_release: app.calc_map(*args)

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

                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"
                                
                                ScrollView:
                                    MDList:
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
                        Tab:
                            id: tab6
                            name: 'tab6'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] Table"
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"
                                
                                ScrollView:
                                    MDList:
                                        id: calc_map



        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
<ItemTable>:
    size_hint_y: None
    height: "42dp"
    
    canvas:
        Color:
            rgba: root.color
        Rectangle:
            size: self.size
            pos: self.pos
    MDLabel:
        text: root.num
        halign: "center"
    MDLabel:
        text: root.date
        halign: "center" 
    MDLabel:
        text: root.payment
        halign: "center" 
    MDLabel:
        text: root.interest
        halign: "center"
    MDLabel:
        text: root.principal
        halign: "center"
    MDLabel:
        text: root.debt
        halign: "center"              

#: import MapView kivy_garden.mapview.MapView
<Exemple_Map>:
    MapView:
        lat: 24.0555
        lon: 90.9802
        zoom: 10
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

class ItemTable(BoxLayout):
    num = StringProperty()
    date = StringProperty()
    payment = StringProperty()
    interest = StringProperty()
    principal = StringProperty()
    debt = StringProperty()
    color = ListProperty()

class Exemple_Map(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# https://stackoverflow.com/questions/2249956/how-to-get-the-same-day-of-next-month-of-a-given-day-in-python-using-datetime
def next_month_date(d):
    _year = d.year + (d.month // 12)
    _month = 1 if (d.month // 12) else d.month + 1
    next_month_len = calendar.monthrange(_year, _month)[1]
    next_month = d
    if d.day > next_month_len:
        next_month = next_month.replace(day=next_month_len)
    next_month = next_month.replace(year=_year, month=_month)
    return next_month

def show_canvas_stress(wid):
    with wid.canvas:
        for x in range(10):
            Color(r(), 1, 1, mode='hsv')
            Rectangle(pos=(r() * wid.width + wid.x, r() * wid.height + wid.y), size=(20, 20))

def draw_graph(wid):
    #print(wid.x, wid.y)
    with wid.canvas:
        Color(.2, .2, .2, 1)
        Line(rectangle=(20, 60, wid.width-20, wid.height-20), width=2)


class KopitinBro(MDApp):
    title = "Kopitin Bro"
    who_is = "Kopitin Boss"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
#        menu_items = [{"viewclass": "IconListItem", "icon": "git", "height": dp(56), "text": f"Item {i}", "on_release": lambda x=f"Item {i}": self.set_item(x),} for i in range(5)]
        menu_items = [{"icon": "format-text-rotation-angle-up", "text": "annuity"},
                      {"icon": "format-text-rotation-angle-down", "text": "differentiated"}]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.payment_type,
            items=menu_items,
            position="auto",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)

        # https://kivymd.readthedocs.io/en/latest/components/pickers/?highlight=date%20picker#
        self.date_dialog = MDDatePicker(
            callback=self.get_date,
            background_color=(0.1, 0.1, 0.1, 1.0),)

    def set_item(self, position_menu, position_menu_item):
        def set_item(interval):
            self.screen.ids.payment_type.text = position_menu_item.text
            position_menu.dismiss()

        Clock.schedule_once(set_item, 0.5)

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
        print(date)
        self.screen.ids.start_date.text = date.strftime("%d-%m-%Y")  # str(date)

    def build(self):
        self.theme_cls.theme_style = "Light"  # "Dark"  # "Light"
        # return Builder.load_string(KV)
        return self.screen
#    def build(self):
#        return Builder.load_string(KV)

    def on_start(self):
        self.screen.ids.start_date.text = datetime.date.today().strftime("%d-%m-%Y")
        self.screen.ids.loan.text = "300000"
        self.screen.ids.months.text = "12"
        self.screen.ids.interest.text = "15"
        self.screen.ids.payment_type.text = "annuity"
        icons_item_menu_lines = {
            "account-cowboy-hat": "?? ????????????",
            "account-multiple": "?? ?????? ??????????????",
            "coffee": "?? ?????? ????????????????????",
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
        # count_icon = instance_tab.icon
        # print it on shell/bash.
        # print(f"Welcome to {count_icon}' tab'" + tab_text)

    def calc_table(self, *args):
        print("button1 pressed")
        start_date = self.screen.ids.start_date.text
        loan = self.screen.ids.loan.text
        months = self.screen.ids.months.text
        interest = self.screen.ids.interest.text
        payment_type = self.screen.ids.payment_type.text
        print(start_date + " " + loan + " " + months + " " + interest + " " + payment_type)
        # convert to date object, float, and so on
        start_date = datetime.datetime.strptime(self.screen.ids.start_date.text, "%d-%m-%Y").date()
        loan = float(loan)
        months = int(months)
        interest = float(interest)

        row_data_for_tab = []
        # annuity payment
        # https://temabiz.com/finterminy/ap-formula-i-raschet-annuitetnogo-platezha.html
        percent = interest / 100 / 12
        monthly_payment = loan * (percent + percent / ((1 + percent) ** months - 1))
        # print(monthly_payment)
        self.screen.ids.calc_data_table.add_widget(ItemTable(
            color = (0.2, 0.8, 0.8, 0.2),
            num = "???",
            date = "Date",
            payment = "Payment",
            interest = "Interest",
            principal = "Principal",
            debt = "Debt"
        ))
        debt_end_month = loan
        for i in range(0, months):
            row_color = (1,1,1,1)
            if (i % 2 != 0):
                row_color = (0.2, 0.2, 0.2, 0.2)
            repayment_of_interest = debt_end_month * percent
            repayment_of_loan_body = monthly_payment - repayment_of_interest
            debt_end_month = debt_end_month - repayment_of_loan_body
            self.screen.ids.calc_data_table.add_widget(ItemTable(
                color = row_color,
                num=str(i+1),
                date = start_date.strftime("%d-%m-%Y"),
                payment = str(round(monthly_payment, 2)),
                interest = str(round(repayment_of_interest, 2)),
                principal = str(round(repayment_of_loan_body, 2)),
                debt = str(round(debt_end_month, 2))
            ))
            start_date = next_month_date(start_date)

        #     print(monthly_payment, repayment_of_interest, repayment_of_loan_body, debt_end_month)
        #     row_data_for_tab.append(
        #         [i + 1, start_date.strftime("%d-%m-%Y"), round(monthly_payment, 2), round(repayment_of_interest, 2),
        #          round(repayment_of_loan_body, 2), round(debt_end_month, 2)])
        # total_amount_of_payments = monthly_payment * months
        # overpayment_loan = total_amount_of_payments - loan
        # effective_interest_rate = ((total_amount_of_payments / loan - 1) / (months / 12)) * 100
        # print(total_amount_of_payments, overpayment_loan, effective_interest_rate)


        #
        # # show_canvas_stress(self.screen.ids.graph)
        # show_canvas_stress(self.screen.ids.chart)
        #
        # self.screen.ids.graph.canvas.clear()
        # draw_graph(self.screen.ids.graph, start_date, loan, months, interest, payment_type)
        #
        # self.screen.ids.chart.canvas.clear()
        # draw_chart(self.screen.ids.chart, total_amount_of_payments, loan)
        #
        # # https://kivymd.readthedocs.io/en/latest/components/datatables/?highlight=datatable
        # data_tables = MDDataTable(
        #     use_pagination=True,
        #     rows_num=10,
        #     column_data=[
        #         ("???", dp(10)),
        #         ("Date", dp(20)),
        #         ("Payment", dp(20)),
        #         ("Interest", dp(20)),
        #         ("Principal", dp(20)),
        #         ("Debt", dp(20)),
        #     ],
        #     row_data=row_data_for_tab,
        # )
        # self.screen.ids.calc_data_table.clear_widgets()
        # self.screen.ids.calc_data_table.add_widget(data_tables)
        # self.screen.ids.calc_data_table.clear_widgets()
        # for i in range(0,100):
        #     row_color = (0,0,0,1)
        #     if (i % 2 != 0):
        #         row_color = (1,1,1,1)
        #     self.screen.ids.calc_data_table.add_widget(
        #         ItemTable(
        #             color = row_color,
        #             text=str(i),
        #         )
        #     )

        show_canvas_stress(self.screen.ids.graph)
        show_canvas_stress(self.screen.ids.chart)
        draw_graph(self.screen.ids.graph)
        pass

    def share_it(self, *args):
        share("title_share", "this content to share!")
    def on_star_click(self):
        print("star clicked!")

    def calc_map(self, *args):
        self.screen.ids.calc_map.add_widget(Exemple_Map())

KopitinBro().run()