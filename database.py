from sqlalchemy import create_engine
import os

from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

db_config = {
    'host': os.getenv('DATABASE_HOST'),
    'user': 'root',
    'password': os.getenv('MYSQL_ROOT_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

print('mariadb+pymysql://' + db_config['user'] + ':' + db_config['password'] + '@' + db_config['host'] + '/' + db_config['database'] + '?charset=utf8mb4')

engine = create_engine(
    'mariadb+pymysql://' + db_config['user'] + ':' + db_config['password'] + '@' + db_config['host'] + '/' + db_config['database'] + '?charset=utf8mb4'
)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    print("Creating tables")
    Base.metadata.create_all(bind=engine)
    return db_session