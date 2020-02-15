import React, { useCallback, useState } from 'react';
import { Line } from 'shared/base/line';
import './uploadZone.scss';
import { useDispatch } from 'react-redux';
import { uploadFileAsync } from 'data/file/action';
import { Icon } from 'shared/base/icon';
import { ActionType } from 'data/actionTypes';

import { RepeatPanel } from './repeatPanel';


export const UploadZone: React.FC = () => {
  const dispatch = useDispatch();

  const [typeFile, setTypeFile] = useState<string>();
  const [file, setFile] = useState<File>();

  const onChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    console.log('upload files');
    setTypeFile(e.target.files[0].name.split('.')[1]);
    setFile(e.target.files[0]);
    uploadFile();
  }, []);

  const uploadFile=useCallback(()=>{
    dispatch(uploadFileAsync({typeFile: typeFile, file: file}));
  },[]);
    
  return (
    <RepeatPanel action={uploadFile} actionType={ActionType.FILE_UPLOADFILE}>
    <Line className="uploadZone">
      <Line className="card container upload-container" justifyContent="around" alignItems="center">
        <form>
         <Line alignItems='center' justifyContent='center'> <Icon className="img-upload" name="upload"></Icon></Line>
          <Line alignItems='center'>
            <input id="file-input" className="input-upload" type="file" onChange={e => onChange(e)}></input>
            <label htmlFor="file-input">Выберите файл  </label>
          </Line>
        </form>
      </Line>
    </Line>
    </RepeatPanel>
  );
};
