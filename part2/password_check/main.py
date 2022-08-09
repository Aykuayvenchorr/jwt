# Просто: Напишите функцию, которая получает пароль 
# в открытом виде первым аргументом и хеш вторым аргументом.
# После чего берет хеш от пароля в открытом виде и сравнивает хеши.
# При хэшировании необходимо использовать алгоритм md5
#
# Для удобства самопроверки мы предоставляем вам пароль в открытом виде:
# H4RDP4S$w0rd
# и хеш в формате md5:
# 80309097b712c6828d0f3f6dfd713e80
#
# ##############################################
# Сложно: Напишите функцию, которая получает пароль 
# в открытом виде, хеш, соль и алгоритм хеширования, 
# берет хеш от пароля в открытом виде и сравнивает хеши
#
# Для самопроверки:
#
# Пароль:
# H4RDP4S$w0rd
#
# Хэш sha256:
# b'\xb6`^\x81q\xd8e\x0b\x1f\x93YR\x8dE\x0c\x0f\xc2\xe4\xbc\x14\xf5\xdf\xdc\xec\xad\xcf\xf3\xca\xd2C\x17\xbb'
#
# Соль:
# Skypro
#
# Число итераций: 1000
import base64
import hashlib
import hmac


def easy(pwd_hash, other_password):
    # TODO Напишите Ваш код здесь
    new_password_hash = hashlib.md5(pwd_hash.encode('utf-8')).hexdigest()
    return new_password_hash == other_password


PWD_HASH_ITERATIONS = 1000


def hard(password_hash, other_password, salt, algo):
    # TODO Напишите Ваш код здесь
    return hmac.compare_digest(
        password_hash,
        hashlib.pbkdf2_hmac(algo, other_password.encode(), salt, PWD_HASH_ITERATIONS)
    )


# print(easy('H4RDP4S$w0rd', '80309097b712c6828d0f3f6dfd713e80'))
# print(hard(b'\xb6`^\x81q\xd8e\x0b\x1f\x93YR\x8dE\x0c\x0f\xc2\xe4\xbc\x14\xf5\xdf\xdc\xec\xad\xcf\xf3\xca\xd2C\x17\xbb',
#            'H4RDP4S$w0rd',
#            'Skypro', 'sha256'))
#
