import { http } from 'core/http';

const baseUrl = 'http://spacehub.su/api';

export function uploadFile(typeFile: string, file: File) {
  return http.post(baseUrl + '/file', { typeFile, file });
}
