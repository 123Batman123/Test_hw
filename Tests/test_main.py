import unittest


from main import max_value, set_list, filter_country, create_folder_ya_disk
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


class TestMaxValue(unittest.TestCase):
    def test_max_value(self):
        res = max_value(stats)
        self.assertEqual(res, 'yandex')

    def test_type(self):
        res = max_value(stats)
        self.assertIsInstance(res, str)

    def test_type_2(self):
        res = max_value(stats)
        self.assertIsInstance(stats, dict)

    def test_in_vk(self):
        res = max_value(stats)
        self.assertIn('vk', stats)


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


class TestSetList(unittest.TestCase):
    def test_check_list(self):
        res = set_list(ids)
        self.assertIsInstance(res, list)

    def test_check_200(self):
        res = set_list(ids)
        self.assertNotIn(200, res)

    @unittest.skip("Пропускаем, нет подозрений, что будет None")
    def test_not_none(self):
        res = set_list(ids)
        self.assertIsNotNone(res)


geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit7': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


class TestFilterCountry(unittest.TestCase):
    def test_in_dict(self):
        res = filter_country(geo_logs)
        self.assertIsInstance(res[-1], dict)

    def test_check_country(self):
        res = filter_country(geo_logs)
        self.assertIs(list(res[-1].values())[0][1], list(res[-2].values())[0][1])


token = ''
path = '/'
name_folder = 'HomeTaskCreateFolder'


class TestYaDisk(unittest.TestCase):
    def test_check_create_folder(self):
        res = create_folder_ya_disk(token, path, name_folder)
        self.assertEqual(res['status_code'], 201)

    def test_check_folder_in_folders(self):
        res = create_folder_ya_disk(token, path, name_folder)
        self.assertIn(name_folder, res['list_requests'])

    @unittest.expectedFailure
    def test_check_50_files(self):
        res = res = create_folder_ya_disk(token, path, name_folder)
        self.assertGreater(len(res['list_requests']), 50, 'Пока файлов меньше 50')


if __name__ == '__main__':
    unittest.main()
