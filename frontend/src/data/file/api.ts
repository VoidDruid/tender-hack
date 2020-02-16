import { http } from 'core/http';
import { RuleType } from 'data/file/models';


const baseUrl = 'http://spacehub.su/api';

export function uploadFile(id: number, file: any) {
  return http.post(baseUrl + '/format_excel', { file }, {id},{ 'contentType': 'multipart/form-data' });
}

export function saveRules(data: RuleType[]) {
  return http.post(baseUrl + '/instructions?id=1', JSON.stringify([...data]));
}

export function getRules() {
  return http.get(baseUrl + '/instructions?id=1');
}
