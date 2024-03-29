import requests
from config import *
from uuid import UUID
from typing import List
from datetime import datetime

class Info:
    seed: str
    results: int
    page: int
    version: str

    def __init__(self, seed: str, results: int, page: int, version: str) -> None:
        self.seed = seed
        self.results = results
        self.page = page
        self.version = version

    def to_dict(self):
        return {
            "seed": self.seed,
            "results": self.results,
            "page": self.page,
            "version": self.version
        }

    @classmethod
    def from_dict(cls, info_dict):
        return cls(
            seed=info_dict.get('seed'),
            results=info_dict.get('results'),
            page=info_dict.get('page'),
            version=info_dict.get('version')
        )


class Dob:
    date: datetime
    age: int

    def __init__(self, date: datetime, age: int) -> None:
        self.date = date
        self.age = age

    def to_dict(self):
        return {
            "date": self.date,
            "age": self.age
        }

    @classmethod
    def from_dict(cls, dob_dict):
        return cls(
            date=dob_dict.get('date'),
            age=dob_dict.get('age')
        )


class ID:
    name: str
    value: None

    def __init__(self, name: str, value: None) -> None:
        self.name = name
        self.value = value

    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value
        }

    @classmethod
    def from_dict(cls, id_dict):
        return cls(
            name=id_dict.get('name'),
            value=id_dict.get('value')
        )


class Coordinates:
    latitude: str
    longitude: str

    def __init__(self, latitude: str, longitude: str) -> None:
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude
        }

    @classmethod
    def from_dict(cls, coordinates_dict):
        return cls(
            latitude=coordinates_dict.get('latitude'),
            longitude=coordinates_dict.get('longitude')
        )


class Street:
    number: int
    name: str

    def __init__(self, number: int, name: str) -> None:
        self.number = number
        self.name = name

    def to_dict(self):
        return {
            "number": self.number,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, street_dict):
        return cls(
            number=street_dict.get('number'),
            name=street_dict.get('name')
        )


class Timezone:
    offset: str
    description: str

    def __init__(self, offset: str, description: str) -> None:
        self.offset = offset
        self.description = description

    def to_dict(self):
        return {
            "offset": self.offset,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, timezone_dict):
        return cls(
            offset=timezone_dict.get('offset'),
            description=timezone_dict.get('description')
        )


class Location:
    street: Street
    city: str
    state: str
    country: str
    postcode: int
    coordinates: Coordinates
    timezone: Timezone

    def __init__(self, street: Street, city: str, state: str, country: str, postcode: int, coordinates: Coordinates,
                 timezone: Timezone) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.postcode = postcode
        self.coordinates = coordinates
        self.timezone = timezone

    def to_dict(self):
        return {
            "street": self.street.to_dict(),
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "postcode": self.postcode,
            "coordinates": self.coordinates.to_dict(),
            "timezone": self.timezone.to_dict()
        }

    @classmethod
    def from_dict(cls, location_dict):
        return cls(
            street=Street.from_dict(location_dict.get('street')),
            city=location_dict.get('city'),
            state=location_dict.get('state'),
            country=location_dict.get('country'),
            postcode=location_dict.get('postcode'),
            coordinates=Coordinates.from_dict(location_dict.get('coordinates')),
            timezone=Timezone.from_dict(location_dict.get('timezone'))
        )


class Login:
    uuid: UUID
    username: str
    password: str
    salt: str
    md5: str
    sha1: str
    sha256: str

    def __init__(self, uuid: UUID, username: str, password: str, salt: str, md5: str, sha1: str, sha256: str) -> None:
        self.uuid = uuid
        self.username = username
        self.password = password
        self.salt = salt
        self.md5 = md5
        self.sha1 = sha1
        self.sha256 = sha256

    def to_dict(self):
        return {
            "uuid": str(self.uuid),
            "username": self.username,
            "password": self.password,
            "salt": self.salt,
            "md5": self.md5,
            "sha1": self.sha1,
            "sha256": self.sha256
        }

    @classmethod
    def from_dict(cls, login_dict):
        return cls(
            uuid=UUID(login_dict.get('uuid')),
            username=login_dict.get('username'),
            password=login_dict.get('password'),
            salt=login_dict.get('salt'),
            md5=login_dict.get('md5'),
            sha1=login_dict.get('sha1'),
            sha256=login_dict.get('sha256')
        )


class Name:
    title: str
    first: str
    last: str

    def __init__(self, title: str, first: str, last: str) -> None:
        self.title = title
        self.first = first
        self.last = last

    def to_dict(self):
        return {
            "title": self.title,
            "first": self.first,
            "last": self.last
        }

    @classmethod
    def from_dict(cls, name_dict):
        return cls(
            title=name_dict.get('title'),
            first=name_dict.get('first'),
            last=name_dict.get('last')
        )


class Picture:
    large: str
    medium: str
    thumbnail: str

    def __init__(self, large: str, medium: str, thumbnail: str) -> None:
        self.large = large
        self.medium = medium
        self.thumbnail = thumbnail

    def to_dict(self):
        return {
            "large": self.large,
            "medium": self.medium,
            "thumbnail": self.thumbnail
        }

    @classmethod
    def from_dict(cls, picture_dict):
        return cls(
            large=picture_dict.get('large'),
            medium=picture_dict.get('medium'),
            thumbnail=picture_dict.get('thumbnail')
        )


class Result:
    gender: str
    name: Name
    location: Location
    email: str
    login: Login
    dob: Dob
    registered: Dob
    phone: str
    cell: str
    id: ID
    picture: Picture
    nat: str

    def __init__(self, gender: str, name: Name, location: Location, email: str, login: Login, dob: Dob, registered: Dob,
                 phone: str, cell: str, id: ID, picture: Picture, nat: str) -> None:
        self.gender = gender
        self.name = name
        self.location = location
        self.email = email
        self.login = login
        self.dob = dob
        self.registered = registered
        self.phone = phone
        self.cell = cell
        self.id = id
        self.picture = picture
        self.nat = nat

    def to_dict(self):
        return {
            "gender": self.gender,
            "name": self.name.to_dict(),
            "location": self.location.to_dict(),
            "email": self.email,
            "login": self.login.to_dict(),
            "dob": self.dob.to_dict(),
            "registered": self.registered.to_dict(),
            "phone": self.phone,
            "cell": self.cell,
            "id": self.id.to_dict(),
            "picture": self.picture.to_dict(),
            "nat": self.nat
        }

    @classmethod
    def from_dict(cls, result_dict):
        return cls(
            gender=result_dict.get('gender'),
            name=Name.from_dict(result_dict.get('name')),
            location=Location.from_dict(result_dict.get('location')),
            email=result_dict.get('email'),
            login=Login.from_dict(result_dict.get('login')),
            dob=Dob.from_dict(result_dict.get('dob')),
            registered=Dob.from_dict(result_dict.get('registered')),
            phone=result_dict.get('phone'),
            cell=result_dict.get('cell'),
            id=ID.from_dict(result_dict.get('id')),
            picture=Picture.from_dict(result_dict.get('picture')),
            nat=result_dict.get('nat')
        )
    
class PersonData:
    results: List[Result]
    info: Info

    def __init__(self, results: List[Result], info: Info) -> None:
        self.results = results
        self.info = info

    def to_dict(self):
        return {
            "results": [result.to_dict() for result in self.results],
            "info": self.info.to_dict()
        }

    @classmethod
    def from_dict(cls, welcome_dict):
        return cls(
            results=[Result.from_dict(result_dict) for result_dict in welcome_dict.get('results')],
            info=Info.from_dict(welcome_dict.get('info'))
        )

def createPerson():
    response = requests.get(url_web)

    if response.status_code == 200:
    # Si la solicitud fue exitosa, puedes acceder a los datos de la respuesta
        data = response.json()  # Convertir la respuesta JSON a un diccionario de Python
        print("Datos obtenidos correctamente:")
        print(data)
        personData =  Result.from_dict(data)
        return personData
        
    else:
    # Si la solicitud no fue exitosa, mostrar un mensaje de error
        print("Error al obtener los datos. Código de estado:", response.status_code)
        print("Mensaje de error:", response.text)
        return None