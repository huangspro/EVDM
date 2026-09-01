```
.
├── ProjectStructure.md
├── README.md
├── UserDatabase
│   └── Users.csv
├── classes.png
├── command.sh
├── packages.png
├── src
│   ├── application
│   │   └── login_register_service
│   │       ├── authentication_code_validation_service.py
│   │       ├── login_service.py
│   │       ├── register_service.py
│   │       └── start_a_meeting_for_theme.py
│   ├── domain
│   │   ├── factories
│   │   │   └── make_domain.py
│   │   ├── model
│   │   │   ├── event.py
│   │   │   ├── meeting.py
│   │   │   ├── meeting_agenda.py
│   │   │   ├── meeting_proposal.py
│   │   │   ├── meeting_theme.py
│   │   │   ├── message.py
│   │   │   ├── user.py
│   │   │   └── vote.py
│   │   ├── repository
│   │   │   ├── meeting_database.py
│   │   │   └── user_database.py
│   │   └── services
│   ├── infrastructure
│   │   └── database
│   │       └── csv_database.py
│   └── utils
│       ├── email_send_service.py
│       ├── status.py
│       └── type.py
└── test
    └── infrastructure
        └── csv_database_test.py

15 directories, 26 files
```
