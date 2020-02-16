import { http } from 'core/http';
import { RuleType } from 'data/file/models';


const baseUrl = 'http://spacehub.su/api';

export function uploadFile(id: number, file: any) {
  return http.post(baseUrl + '/format_excel', { file }, {id},{ 'contentType': 'multipart/form-data' });
}

export function saveRules(data: RuleType[]) {
  const a =[
    null,
    {
    'name': 'offers',
    'type': 'array',
    'fields': [
    {
    'name': 'id',
    'index': 0
    },
    {
    'name': 'name',
    'index': 1
    },
    {
    'name': 'vendor',
    'index': 2,
    'is_optional': true,
    },
    {
    'name': 'Страна происхождения',
    'is_param': true,
    'index': 3
    },
    {
    'name': 'Вид продукции',
    'is_param': true,
    'index': 4
    },
    {
    'name': 'Вид товаров',
    'is_param': true,
    'index': 5
    },
    {
    'name': 'Ширина',
    'index': 6,
    'output': {
    'to': 'dimensions',
    'method': 'x-join'
    }
    },
    {
    'name': 'Длина',
    'index': 7,
    'output': {
    'to': 'dimensions',
    }
    },
    {
    'name': 'Высота',
    'index': 8,
    'output': {
    'to': 'dimensions',
    }
    },
    {
    'name': 'Материал',
    'index': 9,
    'is_param': true
    },
    {
    'name': 'Диаметр',
    'index': 10,
    'is_param': true
    },
    {
    'name': 'expiry',
    'index': 11
    },
    {
    'name': 'Цвет',
    'index': 12,
    'is_param': true
    },
    {
    'name': 'weight',
    'index': 13
    },
    {
    'name': 'Объем',
    'index': 14,
    'is_param': true
    }
    ]
    }
    ];
  return http.post(baseUrl + '/instructions?id=1', JSON.stringify([...a]));
}

export function getRules() {
  return http.get(baseUrl + '/instructions?id=1');
}
