import React, { useState, useCallback, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { Line } from 'shared/base/line';
import { getRulesAsync, saveRulesAsync } from 'data/file/action';
import { EntityControl } from 'app/entityControl';
import { Button } from 'shared/base/button';
import { RuleType, FieldType } from 'data/file/models';
import { TextBoxField } from 'shared/fields/textBoxField';
import { OptionsType } from 'data/model';
import { Icon } from 'shared/base/icon';

import './processControl.scss';

export const ProcessControl: React.FC = () => {
  const [model, setModel] = useState<{ [key: string]: RuleType }>({});
  const [name, setName] = useState<string>();
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getRulesAsync());
  }, []);

  const onSaveCallback = useCallback(() => {
    const a: RuleType[] = [];
    for (const key in model) {
      a.push(model[key]);
    }
    dispatch(saveRulesAsync(a));
  }, [model]);

  const getEntities = useCallback(() => {
    const result: JSX.Element[] = [];
    for (const key in model) {
      result.push(
        <div key={key} className="entity">
          <Line className="titlecard">
            <div className="title">{model[key].name}</div>
            <div
              className="cross"
              onClick={() => {
                const newModel = { ...model };
                delete newModel[key];
                setModel(newModel);
              }}>
              <Icon name="times"></Icon>
            </div>
          </Line>
          <EntityControl
            getModel={(m: { [key: string]: OptionsType }) => {
              const arr: FieldType[] = [];
              for (const key in m) {
                const options = m[key];
                let res: FieldType = { index: options.index, name: key };
                if (options.isMultiple) res.is_multiple = options.isMultiple;
                if (options.parent) res.parent_of = options.parent;
                arr.push(res);
              }
              const k: RuleType = { name: key, type: 'array', fields: arr };
              setModel({ ...model, [key]: k });
            }}
          />
        </div>
      );
    }
    return result;
  }, [model]);

  return (
    <Line className="processControl">
      <Line className="card container">
        <Line justifyContent="between" className="buttonEntity">
          <Line vertical>
            <Line ml="3">
              <h4 className="header">Параметры для парсера</h4>
            </Line>
            <Line ml="3" className="text-field" justifyContent="between">
              <Line>
                {' '}
                <TextBoxField name="" value={name} onChange={(value: string) => setName(value)}></TextBoxField>
                <Button
                  label="Добавить сущность"
                  onClick={() => {
                    if (name && name != '') {
                      const newModel = { ...model, [name]: { name, type: 'array', fields: [] } };
                      setModel(newModel);
                    }
                    setName('');
                  }}
                  buttonType="primary"
                  className="addEntityButton"></Button>
              </Line>
              <Button
                label="Сохранить"
                ml="5"
                onClick={onSaveCallback}
                buttonType="primary"
                className="saveButton"></Button>
            </Line>
            <Line vertical className="list-entity">
              {getEntities()}
            </Line>
          </Line>
        </Line>
      </Line>
    </Line>
  );
};
