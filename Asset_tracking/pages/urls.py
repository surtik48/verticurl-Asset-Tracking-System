from django.contrib.admin.decorators import register
from django.urls import path
from . import views

urlpatterns=[

    path('index/',views.index,name='index'),
    path('index2/',views.index2,name='index2'),
    path('accordions/',views.accordions,name='accordions'),
    path('badges/',views.badges,name='badges'),
    path('breadcrumbs/',views.breadcrumbs,name='breadcrumbs'),
    path('buttons/',views.buttons,name='buttons'),
    path('carousel/',views.carousel,name='carousel'),
    path('clipboard/',views.clipboard,name='clipboard'),
    path('colcade/',views.colcade,name='colcade'),
    path('contextmenu/',views.contextmenu,name='contextmenu'),
    path('dragula/',views.dragula,name='dragula'),
    path('dropdowns/',views.dropdowns,name='dropdowns'),
    path('loaders/',views.loaders,name='loaders'),
    path('modals/',views.modals,name='modals'),
    path('notifications/',views.notifications,name='notifications'),
    path('pagination/',views.pagination,name='pagination'),
    path('popups/',views.popups,name='popups'),
    path('progress/',views.progress,name='progress'),
    path('slider/',views.slider,name='slider'),
    path('tabs/',views.tabs,name='tabs'),
    path('tooltips/',views.tooltips,name='tooltips'),
    path('typography/',views.typography,name='typography'),

    path('basic-table/',views.basictable,name='basic-table'),
    path('data-table/',views.datatable,name='data-table'),
    path('js-grid/',views.jsgrid,name='js-grid'),
    path('sortable-table/',views.sortabletable,name='sortable-table'),
    path('widgets/',views.widgets,name='widgets'),

    path('calendar/',views.calendar,name='calendar'),
    path('email/',views.email,name='email'),
    path('gallery/',views.gallery,name='gallery'),
    path('todo/',views.todo,name='todo'),

    path('c3/',views.c3,name='c3'),
    path('chartist/',views.chartist,name='chartist'),
    path('chartjs/',views.chartjs,name='chartjs'),
    path('flot-chart/',views.flotchart,name='flot-chart'),
    path('google-charts/',views.googlecharts,name='google-charts'),
    path('justGage/',views.justGage,name='justGage'),
    path('morris/',views.morris,name='morris'),
    path('sparkline/',views.sparkline,name='sparkline'),

    path('advanced_elements/',views.advanced_elements,name='advanced_elements'),
    path('basic_elements/',views.basic_elements,name='basic_elements'),
    path('code_editor/',views.code_editor,name='code_editor'),
    path('dropify/',views.dropify,name='dropify'),
    path('text_editor/',views.text_editor,name='text_editor'),
    path('validation/',views.validation,name='validation'),
    path('wizard/',views.wizard,name='wizard'),

    path('flag-icons/',views.flagicons,name='flag-icons'),
    path('font-awesome/',views.fontawesome,name='font-awesome'),
    path('mdi/',views.mdi,name='mdi'),
    path('simple-line-icon/',views.simplelineicon,name='simple-line-icon'),
    path('themify/',views.themify,name='themify'),

    path('google-maps/',views.googlemaps,name='google-maps'),
    path('mapael/',views.mapael,name='mapael'),
    path('vector-map/',views.vectormap,name='vector-map'),

    path('rtl/',views.rtl,name='rtl'),


    path('blank-page/',views.blankpage,name='blank-page'),
    path('error-404/',views.error404,name='error-404'),
    path('error-500/',views.error500,name='error-500'),
    path('faq/',views.faq,name='faq'),
    path('faq-2/',views.faq2,name='faq-2'),
    path('invoice/',views.invoice,name='invoice'),
    path('lock-screen/',views.lockscreen,name='lock-screen'),
    path('login/',views.login,name='login'),
    path('login-2/',views.login2,name='login-2'),
    path('news-grid/',views.newsgrid,name='news-grid'),
    path('orders/',views.orders,name='orders'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('pricing-table/',views.pricingtable,name='pricing-table'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('register-2/',views.register2,name='register-2'),
    path('search-results/',views.searchresults,name='search-results'),
    path('timeline/',views.timeline,name='timeline'),

]

