from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivy.uix.floatlayout import FloatLayout
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

print(locale.getdefaultlocale())


import gettext
from os.path import dirname, join

KV = '''
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts



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
                                        hint_text: 'Start date'
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
                                        hint_text: "Interest, %"
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
                                        disabled: True

                                    MDIconButton:
                                        icon: 'format-text-rotation-angle-up'
                                        on_press: app.change_payment_type()


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
                                        text: 'Graph payments'
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
                                        text: 'Interest'
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"

                                    MDIcon:
                                        icon: "checkbox-blank"
                                        halign: "right"
                                        color: 1, 0, 0, 1

                                    MDLabel:
                                        text: 'Principal'
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
                                        text: 'Chart payments'
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
                                        text: 'Interest'
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"

                                    MDIcon:
                                        icon: "checkbox-blank"
                                        halign: "right"
                                        color: 1, 0, 0, 1

                                    MDLabel:
                                        text: 'Principal'
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"



                        Tab:
                            id: tab5
                            name: 'tab5'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['book-open-variant']}[/size][/font] Sum"

                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    spacing: "10dp"

                                    MDLabel:
                                        text: 'Property value'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_property_value_label
                                        halign: "left"

                                    MDLabel:
                                        text: 'Monthly payment'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_payment_label
                                        halign: "left"

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    spacing: "10dp"

                                    MDLabel:
                                        text: 'Interest'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_interest_label
                                        halign: "left"

                                    MDLabel:
                                        text: 'Total interest'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_overpayment_loan_label
                                        halign: "left"

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    spacing: "10dp"

                                    MDLabel:
                                        text: 'Start date'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_start_date_label
                                        halign: "left"

                                    MDLabel:
                                        text: 'Payments type'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_payments_type_label
                                        halign: "left"

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    spacing: "10dp"

                                    MDLabel:
                                        text: 'End date'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_end_date_label
                                        halign: "left"

                                    MDLabel:
                                        text: "Effective %"
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_effective_interest_rate_label
                                        halign: "left"

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    spacing: "10dp"

                                    MDLabel:
                                        text: 'Total payments'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_total_amount_of_payments_label
                                        halign: "left"

                                    MDLabel:
                                        text: 'Term length'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_term_length_label
                                        halign: "left"



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


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class ContentDialogSend(BoxLayout):
    pass


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


# https://kivy.org/doc/stable/examples/gen__canvas__canvas_stress__py.html
def show_canvas_stress(wid):
    with wid.canvas:
        for x in range(10):
            Color(r(), 1, 1, mode='hsv')
            Rectangle(pos=(r() * wid.width + wid.x, r() * wid.height + wid.y), size=(20, 20))


def draw_graph(wid, start_date, loan, months, interest, payment_type):
    # print(wid.x, wid.y)
    with wid.canvas:
        Color(.2, .2, .2, 1)
        Line(rectangle=(wid.x, wid.y, wid.width, wid.height), width=1)
    graph_height = wid.height
    delta_width = wid.width / months

    percent = interest / 100 / 12
    monthly_payment = loan * (percent + percent / ((1 + percent) ** months - 1))

    debt_end_month = loan
    for i in range(0, months):
        repayment_of_interest = debt_end_month * percent
        repayment_of_loan_body = monthly_payment - repayment_of_interest
        debt_end_month = debt_end_month - repayment_of_loan_body
        delta_height_interest = int(repayment_of_interest * graph_height / monthly_payment)
        delta_height_loan = int(repayment_of_loan_body * graph_height / monthly_payment)
        # print("####: ", delta_height_loan, delta_height_loan)
        # print(monthly_payment, repayment_of_interest, repayment_of_loan_body, debt_end_month)
        with wid.canvas:
            Color(1, 0, 0, 1)
            Rectangle(pos=(wid.x + int(i * delta_width), wid.y), size=(int(delta_width), delta_height_loan))
            Color(0, 0, 1, 1)
            Rectangle(pos=(wid.x + int(i * delta_width), wid.y + delta_height_loan),
                      size=(int(delta_width), delta_height_interest))


def draw_chart(wid, total_amount_of_payments, loan):
    interest_chart = ((total_amount_of_payments - loan) * 360) / total_amount_of_payments
    circle_width = wid.width
    center_x = 0
    center_y = wid.height // 2 - circle_width // 2
    if (wid.width > wid.height):
        circle_width = wid.height
        center_x = wid.width // 2 - circle_width // 2
        center_y = 0
    # print(wid.x, wid.y)
    with wid.canvas:
        Color(0, 0, 1, 1)
        Ellipse(pos=(wid.x + center_x, wid.y + center_y), size=(circle_width, circle_width),
                angle_start=360 - int(interest_chart), angle_end=360)
        Color(1, 0, 0, 1)
        Ellipse(pos=(wid.x + center_x, wid.y + center_y), size=(circle_width, circle_width), angle_start=0,
                angle_end=360 - int(interest_chart))

class MortgageCalculator(MDApp):
    title = "Mortgage Calculator"
    by_who = "by Demyan Shvetsov"
    dialog = None
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

        # https://kivymd.readthedocs.io/en/latest/components/pickers/?highlight=date%20picker#
        self.date_dialog = MDDatePicker()
        self.date_dialog.bind(on_release=self.get_date, on_save=self.on_save)

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

    def change_payment_type(self):
        if self.screen.ids.payment_type.text == 'annuity':
            self.screen.ids.payment_type.text = 'differentiated'
            self.data_for_calc_is_changed = True
            self.payment_annuity = False
            self.calc_1st_screen()
        else:
            self.screen.ids.payment_type.text = 'annuity'
            self.data_for_calc_is_changed = True
            self.payment_annuity = True
            self.calc_1st_screen()

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        x = str(value).split('-')
        x = x[::-1]
        self.screen.ids.start_date.text = str('-'.join(x))

        print(instance, value, date_range)

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

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
        pre_start_date = datetime.datetime.strptime(self.screen.ids.start_date.text, "%d-%m-%Y").date()
        print("Before: ", date, self.data_for_calc_is_changed, pre_start_date == date)
        self.screen.ids.start_date.text = date.strftime("%d-%m-%Y")  # str(date)
        if (pre_start_date != date):
            self.data_for_calc_is_changed = True
        print("After: ", date, self.data_for_calc_is_changed, pre_start_date == date)

    def build(self):
        self.theme_cls.theme_style = "Light"
        return self.screen
    
    def calc_1st_screen(self):
        if self.screen.ids.loan.text.isnumeric():
            if float(self.screen.ids.loan.text) > 1:
                loan = float(self.screen.ids.loan.text)
            else:
                loan = 50000.0
                self.screen.ids.loan.text = '50000'
        else:
            loan = 50000.0
            self.screen.ids.loan.text = '50000'

        if self.screen.ids.months.text.isnumeric():
            if int(self.screen.ids.months.text) > 1:
                months = int(self.screen.ids.months.text)
            else:
                months = 12
                self.screen.ids.months.text = '12'
        else:
            months = 12
            self.screen.ids.months.text = '12'

        if self.screen.ids.interest.text.isnumeric():
            if (float(self.screen.ids.interest.text) > 1) :
                interest = float(self.screen.ids.interest.text)
            else:
                interest = 22.0
                self.screen.ids.interest.text = '22.0'
        else:
            interest = 22.0
            self.screen.ids.interest.text = '22.0'

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

        self.calc_1st_screen()
        icons_item_menu_lines = {
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
        # def on_tab_switch(self, instance_tabs, instance_tab, instance_tabs_label, tab_text):
        '''Called when switching tabs.

                :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
                :param instance_tab: <__main__.Tab object>;
                :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
                :param tab_text: text or name icon of tab;
                '''
        # print(instance_tab.name + " : " + tab_text)
        self.current_tab = args[1].name
        # print(args)
        # print("tab clicked!" + instance_tab.ids.label.text)
        ############# instance_tab.ids.label.text = tab_text
        # print(instance_tab.ids.label.text)
        if self.data_for_calc_is_changed:
            self.calc_table(self, args)
            self.data_for_calc_is_changed = False
        pass

    def on_star_click(self):
        pass

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

        next_date = start_date
        next_prev_date = next_date

        min_monthly_payment = 0
        max_monthly_payment = 0

        if self.payment_annuity:
            monthly_payment = loan * (percent + percent / ((1 + percent) ** months - 1))
            # print(monthly_payment)
            debt_end_month = loan
            for i in range(0, months):
                repayment_of_interest = debt_end_month * percent
                repayment_of_loan_body = monthly_payment - repayment_of_interest
                debt_end_month = debt_end_month - repayment_of_loan_body
                # print(monthly_payment, repayment_of_interest, repayment_of_loan_body, debt_end_month)
                row_data_for_tab.append(
                    [i + 1, next_date.strftime("%d-%m-%Y"), round(monthly_payment, 2), round(repayment_of_interest, 2),
                     round(repayment_of_loan_body, 2), round(debt_end_month, 2)])
                next_prev_date = next_date
                next_date = next_month_date(next_date)
            total_amount_of_payments = monthly_payment * months
            overpayment_loan = total_amount_of_payments - loan
            effective_interest_rate = ((total_amount_of_payments / loan - 1) / (months / 12)) * 100
            # print(total_amount_of_payments, overpayment_loan, effective_interest_rate)
        else:
            repayment_of_interest = loan * percent
            repayment_of_loan_body = loan / months
            max_monthly_payment = repayment_of_interest + repayment_of_loan_body
            # print(monthly_payment)
            total_amount_of_payments = 0
            overpayment_loan = 0
            debt_end_month = loan
            for i in range(0, months):
                repayment_of_interest = debt_end_month * percent
                debt_end_month = debt_end_month - repayment_of_loan_body
                monthly_payment = repayment_of_interest + repayment_of_loan_body
                total_amount_of_payments += monthly_payment
                overpayment_loan += repayment_of_interest
                # print(monthly_payment, repayment_of_interest, repayment_of_loan_body, debt_end_month)
                row_data_for_tab.append(
                    [i + 1, next_date.strftime("%d-%m-%Y"), round(monthly_payment, 2), round(repayment_of_interest, 2),
                     round(repayment_of_loan_body, 2), round(debt_end_month, 2)])
                next_prev_date = next_date
                next_date = next_month_date(next_date)
            min_monthly_payment = monthly_payment

            effective_interest_rate = ((total_amount_of_payments / loan - 1) / (months / 12)) * 100
            # print(total_amount_of_payments, overpayment_loan, effective_interest_rate)

        # show_canvas_stress(self.screen.ids.graph)
        show_canvas_stress(self.screen.ids.chart)

        # tab3
        self.screen.ids.graph.canvas.clear()
        draw_graph(self.screen.ids.graph, start_date, loan, months, interest, payment_type)

        # tab4
        self.screen.ids.chart.canvas.clear()
        draw_chart(self.screen.ids.chart, total_amount_of_payments, loan)

        # tab2
        # https://kivymd.readthedocs.io/en/latest/components/datatables/?highlight=datatable
        self.data_tables = MDDataTable(
            use_pagination=True,
            pagination_menu_pos='center',
            rows_num=10,
            column_data=[
                ("№", dp(10)),
                ('Date', dp(20)),
                ('Payment', dp(20)),
                ('Interest', dp(20)),
                ('Principal', dp(20)),
                ('Debt', dp(20)),
            ],
            row_data=row_data_for_tab,
        )
        self.screen.ids.calc_data_table.clear_widgets()
        self.screen.ids.calc_data_table.add_widget(self.data_tables)

        # tab5
        if self.payment_annuity:
            self.screen.ids.sum_payment_label.text = str(round(monthly_payment, 2))
        else:
            self.screen.ids.sum_payment_label.text = str(round(min_monthly_payment, 2)) + " ... " + str(round(max_monthly_payment, 2))

        self.screen.ids.sum_total_amount_of_payments_label.text = str(round(total_amount_of_payments, 2))
        self.screen.ids.sum_overpayment_loan_label.text = str(round(overpayment_loan, 2))
        self.screen.ids.sum_effective_interest_rate_label.text = str(round(effective_interest_rate, 2))

        self.screen.ids.sum_term_length_label.text = str(round(months, 2)) + " months"
        self.screen.ids.sum_interest_label.text = str(round(interest, 2)) + " %"
        self.screen.ids.sum_property_value_label.text = str(round(loan, 2))

        self.screen.ids.sum_start_date_label.text = start_date.strftime("%d-%m-%Y")
        self.screen.ids.sum_end_date_label.text = next_prev_date.strftime("%d-%m-%Y")

        self.screen.ids.sum_payments_type_label.text = payment_type

        pass

MortgageCalculator().run()