
import traverse_invoke
import yaml
traverse_invoke.enable_logging()


funcs = {
    'CRM systems':{
        'Hubspot': {
            'create lead':lambda **data: print('Lead data', data)
            ,'create deal':lambda **data: print('Deal data', data)
            }
        ,'Salesforce': {
            'create lead':lambda **data: print('Salesforce lead data', data)
            ,'create deal':lambda **data: print('Salesforce deal data', data)
            }

        }
}

data = yaml.safe_load(
    '''
    Leads:
        - name: Mark
          phone: 111210111
          Salesforce:
            phone: 1000000000
            create deal:
                phone: 10012000
          Hubspot:
            name: Mark Twain
    '''
                  )

def create_deals():
    print(data)
    for lead in data['Leads']:
        fpath = 'CRM systems.Hubspot.create lead.Salesforce.create lead'

        traverse_invoke.entry_traverse(lead, fpath.split('.'), funcs)


if __name__=='__main__':
    create_deals()
