```
.
├── api
├── command.sh
├── ProjectStructure.md
├── README.md
├── src
│   ├── application
│   │   └── login_register_service
│   │       ├── authentication_code_validation_service.py
│   │       ├── login_service.py
│   │       └── register_service.py
│   ├── domain
│   │   ├── factories
│   │   │   └── make_domain.py
│   │   ├── message
│   │   │   └── message.py
│   │   ├── model
│   │   │   ├── event.py
│   │   │   ├── meeting_agenda.py
│   │   │   ├── meeting_proposal.py
│   │   │   ├── meeting.py
│   │   │   ├── meeting_theme.py
│   │   │   ├── user.py
│   │   │   └── vote.py
│   │   ├── repository
│   │   │   ├── meeting_database.py
│   │   │   └── user_database.py
│   │   └── services
│   ├── infrastructure
│   │   ├── database
│   │   │   └── csv_database.py
│   │   ├── email_service
│   │   └── message
│   │       ├── picture_message.py
│   │       └── test_message.py
│   └── utils
│       ├── email_send_service.py
│       ├── status.py
│       └── type.py
├── test
│   ├── application
│   ├── domain
│   └── infrastructure
│       └── csv_database_test.py
└── UserDatabase
    └── Users.csv

21 directories, 25 files
```
