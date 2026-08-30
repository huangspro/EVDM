.
├── api
├── command.sh
├── ProjectStructure.md
├── README.md
├── src
│   ├── application
│   ├── domain
│   │   ├── factories
│   │   │   └── make_domain.py
│   │   ├── message
│   │   │   └── message.py
│   │   ├── model
│   │   │   ├── event.py
│   │   │   ├── user.py
│   │   │   └── vote.py
│   │   ├── repository
│   │   │   └── user_database.py
│   │   └── services
│   ├── infrastructure
│   │   ├── database
│   │   │   └── csv_database.py
│   │   └── message
│   │       ├── picture_message.py
│   │       └── test_message.py
│   └── utils
│       ├── status.py
│       └── type.py
├── test
│   ├── application
│   ├── domain
│   └── infrastructure
│       └── csv_database_test.py
└── UserDatabase
    └── Users.csv

19 directories, 16 files
