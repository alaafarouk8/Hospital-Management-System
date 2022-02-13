{
    'name': "iti_hms",
    'summary': "summary about hms"
    ,
    'description': """
    Description text
    """,
    'depends': ['base', 'crm'],
    # data files always loaded at installation
    'data': [
        'views/hms_patient_view.xml',
        'views/hms_departments_view.xml',
        'views/hms_doctor_view.xml',
        'views/hms_log_history.xml',
        'views/crm_inherit_view.xml'
    ],

}


