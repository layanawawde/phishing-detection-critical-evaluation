from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, fbeta_score, matthews_corrcoef, roc_auc_score, confusion_matrix

def metrics(model,X,y):
    pred=model.predict(X)
    score=model.predict_proba(X)[:,1]
    tn,fp,fn,tp=confusion_matrix(y,pred,labels=[-1,1]).ravel()
    return {'accuracy':accuracy_score(y,pred),'precision':precision_score(y,pred),'recall':recall_score(y,pred),'f1':f1_score(y,pred),'f2':fbeta_score(y,pred,beta=2),'mcc':matthews_corrcoef(y,pred),'roc_auc':roc_auc_score((y==1).astype(int),score),'tn':int(tn),'fp':int(fp),'fn':int(fn),'tp':int(tp)}
