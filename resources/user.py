from flask_restful import Resource
from flask import request
import mysql.connector
from mysql.connector import Error

from mysql_connection import get_connection

from email_validator import validate_email, EmailNotValidError

from resources.utll import check_password, hash_password

from flask_jwt_extended import create_access_token, get_jwt, jwt_required

import datetime

