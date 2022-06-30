from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons

from kivymd.uix.label import MDLabel

from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock

from kivymd.uix.pickers import MDDatePicker
import datetime
import calendar

from kivy.graphics import Color, Rectangle, Line, Ellipse
from random import random as r

from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.uix.textinput import TextInput

import locale

KV = '''
# https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts

# https://github.com/tito/kivy-gettext-example
# this import for multilingual support

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
        text: app.by_who
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
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
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
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] "+'Input'

                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calendar-month"

                                    MDTextField:
                                        id: start_date
                                        hint_text: 'Start date'
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
                                        name: 'loan'
                                        hint_text: 'Loan'
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'float'
                                        helper_text_mode: "on_focus"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "clock-time-five-outline"

                                    MDTextField:
                                        id: months
                                        name: 'months'
                                        hint_text: 'Months'
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'int'
                                        helper_text_mode: "on_focus"


                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "bank"

                                    MDTextField:
                                        id: interest
                                        name: 'interest'
                                        hint_text: 'Interest' +", %"
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'float'
                                        helper_text_mode: "on_focus"

                                    MDTextField:
                                        id: payment_type
                                        name: 'payment_type'
                                        hint_text: 'Payment type'
                                        text: "annuity"
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1


                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: 'Monthly payment'

                                    MDTextField:
                                        id: payment_label
                                        hint_text: ""
                                        disabled: True

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: 'Total interest'

                                    MDTextField:
                                        id: overpayment_loan_label
                                        hint_text: ""
                                        disabled: True

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: 'Total payments'

                                    MDTextField:
                                        id: total_amount_of_payments_label
                                        hint_text: ""
                                        disabled: True

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: 'Effective'+" %"

                                    MDTextField:
                                        id: effective_interest_rate_label
                                        hint_text: ""
                                        disabled: True
                                        text_hint_color:[0,0,1,1]

                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] "+'Table'

                        Tab:
                            id: tab3
                            name: 'tab3'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/size][/font] "+'Graph'

                        Tab:
                            id: tab4
                            name: 'tab4'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] "+'Chart'

                        Tab:
                            id: tab5
                            name: 'tab5'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['book-open-variant']}[/size][/font] "+'Sum'


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

        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class MortgageCalculator(MDApp):
    title = "MortgageCalculator"
    by_who = "Demyan Shvetsov"
    dialog = None
    lang = StringProperty('en')
    data_tables = None
    current_tab = 'tab1'
    payment_annuity = True
    menu = None # for recreate menu on lang change

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.primary_hue = "A100"
        self.data_for_calc_is_changed = True

        self.screen = Builder.load_string(KV)

        menu_items = [{"icon": "format-text-rotation-angle-up", "text": 'annuity'},
                      {"icon": "format-text-rotation-angle-down", "text": 'differentiated'}]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.payment_type,
            items=menu_items,
            position="auto",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)

        self.screen.ids.loan.bind(
            on_touch_down=self.validate_on_nums_input,
            focus=self.on_focus,
        )

        self.screen.ids.months.bind(
            on_touch_down=self.validate_on_nums_input,
            focus=self.on_focus,
        )

        self.screen.ids.interest.bind(
            on_touch_down=self.validate_on_nums_input,
            focus=self.on_focus,
        )

    def on_focus(self, instance, value):
        if value:
            print('User focused', instance.name, instance.text)
            if instance.name == 'loan':
                self.screen.ids.loan.helper_text = "Please enter only numbers, max 999 999 999"
            elif instance.name == 'months':
                self.screen.ids.months.helper_text = "Please enter only numbers, max 1200"
            elif instance.name == 'interest':
                self.screen.ids.interest.helper_text = "Please enter only numbers, max 1000"
        else:
            print('User defocused', instance.name, instance.text)
            if instance.name == 'loan':
                self.screen.ids.loan.helper_text = ""
                if len(self.screen.ids.loan.text) > 9:
                    self.screen.ids.loan.text = self.screen.ids.loan.text[0:9]
                self.calc_1st_screen()
                self.data_for_calc_is_changed = True
            elif instance.name == 'months':
                self.screen.ids.months.helper_text = ""
                if len(self.screen.ids.months.text) > 4:
                    self.screen.ids.months.text = self.screen.ids.months.text[0:4]
                if self.screen.ids.months.text.isnumeric():
                    if int(self.screen.ids.months.text) > 1200:
                        self.screen.ids.months.text = "1200"
                self.calc_1st_screen()
                self.data_for_calc_is_changed = True
            elif instance.name == 'interest':
                self.screen.ids.interest.helper_text = ""
                if len(self.screen.ids.interest.text) > 4:
                    self.screen.ids.interest.text = self.screen.ids.interest.text[0:4]
                if self.screen.ids.interest.text.isnumeric():
                    if float(self.screen.ids.interest.text) > 1000:
                        self.screen.ids.interest.text = "1000"
                self.calc_1st_screen()
                self.data_for_calc_is_changed = True

    def validate_on_nums_input(self, instance_textfield, value):
        print(instance_textfield, value)
        # self.screen.ids.loan.error = True

    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.screen.ids.payment_type.text = instance_menu_item.text
            instance_menu.dismiss()
            before_change = self.payment_annuity
            if self.screen.ids.payment_type.text == 'annuity':
                self.payment_annuity = True
            else:
                self.payment_annuity = False
            print(self.payment_annuity)
            if before_change != self.payment_annuity:
                print("value is changed for payment type")
                self.calc_1st_screen()
                self.data_for_calc_is_changed = True

        Clock.schedule_once(set_item, 0.5)

    def build(self):
        self.theme_cls.theme_style = "Light"
        return self.screen

    def calc_1st_screen(self):
        if self.screen.ids.loan.text.isnumeric():
            if float(self.screen.ids.loan.text) > 1:
                loan = float(self.screen.ids.loan.text)
            else:
                loan = 1.0
                self.screen.ids.loan.text = '1'
        else:
            loan = 1.0
            self.screen.ids.loan.text = '1'

        if self.screen.ids.months.text.isnumeric():
            if int(self.screen.ids.months.text) > 1:
                months = int(self.screen.ids.months.text)
            else:
                months = 1
                self.screen.ids.months.text = '1'
        else:
            months = 1
            self.screen.ids.months.text = '1'

        if self.screen.ids.interest.text.isnumeric():
            if (float(self.screen.ids.interest.text) > 1) :
                interest = float(self.screen.ids.interest.text)
            else:
                interest = 1.0
                self.screen.ids.interest.text = '1'
        else:
            interest = 1
            self.screen.ids.interest.text = '1'

        percent = interest / 100 / 12

        if self.payment_annuity:
            monthly_payment = loan * (percent + percent / ((1 + percent) ** months - 1))
            total_amount_of_payments = monthly_payment * months
            overpayment_loan = total_amount_of_payments - loan
            effective_interest_rate = ((total_amount_of_payments / loan - 1) / (months / 12)) * 100
            self.screen.ids.payment_label.text = str(round(monthly_payment, 2))
        else:
            repayment_of_interest = loan * percent
            repayment_of_loan_body = loan / months
            max_monthly_payment = repayment_of_interest + repayment_of_loan_body

            total_amount_of_payments = 0
            overpayment_loan = 0

            debt_end_month = loan
            for i in range(0, months):
                repayment_of_interest = debt_end_month * percent
                debt_end_month = debt_end_month - repayment_of_loan_body
                monthly_payment = repayment_of_interest + repayment_of_loan_body
                total_amount_of_payments += monthly_payment
                overpayment_loan += repayment_of_interest
            min_monthly_payment = monthly_payment

            effective_interest_rate = ((total_amount_of_payments / loan - 1) / (months / 12)) * 100
            self.screen.ids.payment_label.text = str(round(min_monthly_payment, 2)) + " ... " + str(round(max_monthly_payment, 2))

        #self.screen.ids.payment_label.text = str(round(monthly_payment, 2))
        self.screen.ids.total_amount_of_payments_label.text = str(round(total_amount_of_payments, 2))
        self.screen.ids.overpayment_loan_label.text = str(round(overpayment_loan, 2))
        self.screen.ids.effective_interest_rate_label.text = str(round(effective_interest_rate, 2))

    def on_start(self):
        self.screen.ids.start_date.text = datetime.date.today().strftime("%d-%m-%Y")
        self.screen.ids.loan.text = "50000"
        self.screen.ids.months.text = "12"
        self.screen.ids.interest.text = "22"
        #self.screen.ids.payment_type.text = "annuity"

        self.calc_1st_screen()
        icons_item_menu_lines = {
            "account-cowboy-hat": "About author",
            "github": "Source code",
            "shield-sun": "Dark/Light",
        }
        icons_item_menu_tabs = {
            "calculator-variant": "Input",
            "table-large": "Table",
            "chart-areaspline": "Graph",
            "chart-pie": "Chart",
            "book-open-variant": "Sum",
        }
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )

        # To auto generate tabs
        # for icon_name, name_tab in icons_item_menu_tabs.items():
        #     self.root.ids.tabs.add_widget(
        #         Tab(
        #             text=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/size][/font] {name_tab}"
        #         )
        #     )

        pass

    def on_tab_switch(self, *args):
        '''Called when switching tabs.

                :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
                :param instance_tab: <__main__.Tab object>;
                :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
                :param tab_text: text or name icon of tab;
                '''
        self.current_tab = args[1].name
        pass

MortgageCalculator().run()