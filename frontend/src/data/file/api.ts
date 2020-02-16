import { http } from 'core/http';
import { RuleType } from 'data/file/models';

const baseUrl = 'http://spacehub.su/api';

export function uploadFile(typeFile: string, file: File) {
  return http.post(baseUrl + '/file', { typeFile, file });
}

export function saveRules(data: RuleType[]) {
  return http.post(baseUrl + '/instructions?id=1', JSON.stringify([...data]));
}

export function getRules() {
  return http.get(baseUrl + '/instructions?id=1');
}
