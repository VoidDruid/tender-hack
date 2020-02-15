import React, { useState } from 'react';
import { Line } from 'shared/base/line';
import { TextBoxField } from 'shared/fields/textBoxField';
import { Button } from 'shared/base/button';
import { List } from 'app/list';
import { OptionsType } from 'data/model';

import './processControl.scss';

export const ProcessControl: React.FC = () => {
  type ModelType = { [key: string]: OptionsType };
  const [model, setModel] = useState<ModelType>({});
  const [name, setName] = useState<string>();

  return (
    <Line className="processControl">
      <Line className="card container" vertical>
        <Line>
          <TextBoxField name="" value={name} onChange={(value: string) => setName(value)}></TextBoxField>
          <Button
            className="button"
            buttonType='primary'
            label="Add"
            onClick={() => {
              if (name && name != '') {
                setModel({
                  ...model,
                  [`${name}`]: {}
                });
                setName('');
              }
            }}></Button>
        </Line>
        <Line vertical>
          <List
            options={model}
            onAddOptions={(key:string, options: OptionsType) => {}}
            onDelete={(key: string) => {
              const newModel = { ...model };
              delete newModel[key];
              setModel(newModel);
            }}
          />
        </Line>
      </Line>
    </Line>
  );
};
