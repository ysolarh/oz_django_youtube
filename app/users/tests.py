from django.test import TestCase
from django.contrib.auth import get_user_model  # django에서 제공하는 기본 인증


class UserTestCase(TestCase):
    # 회원가입을 가정 => 회원가입 함수 테스트 코드 작성
    # 이메일과 패스워드 입력받고, 회원가입이 정상적으로 잘 이뤄졌는지 체크

    def test_create_user(self):
        email = 'example@gm.com'
        password = 'password'

        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        email = 'example@gm.com'
        password = 'password'
        super_user = get_user_model().objects.create_superuser(
            email=email, password=password
        )
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
