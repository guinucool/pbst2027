import pandas as pd

def pd_to_label(df):
    
    label = dict()
    
    for row in df.itertuples(index=False):
        
        llm = row.LLM
        domain = row.ThirdParty_Domain
        organization = row.Organization
        tracking = row.Tracking
        
        if llm not in label:
            label[llm] = dict()
            
        label[llm][domain] = (organization, tracking)
        
    return label

def label_all(path_collector, path_labelled):
    
    collector = pd.read_csv(path_collector)
    labelled = pd_to_label(pd.read_csv(path_labelled))
    
    collector['Organization'] = collector.apply(lambda row: labelled[row['LLM']][row['ThirdParty_Domain']][0], axis=1)
    collector['Tracking'] = collector.apply(lambda row: labelled[row['LLM']][row['ThirdParty_Domain']][1], axis=1)
    
    return collector