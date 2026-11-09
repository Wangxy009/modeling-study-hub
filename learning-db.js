const LearningDB=(()=>{
  const KEY='modelWriterLearningDB_v2';
  const empty=()=>({sessions:[],profile:{name:'数学建模写手',goal:'能独立完成国赛论文的审题、论证与表达'},version:1});
  const read=()=>{try{return {...empty(),...JSON.parse(localStorage.getItem(KEY)||'null')}}catch{return empty()}};
  const write=db=>localStorage.setItem(KEY,JSON.stringify(db));
  const uid=()=>`${Date.now()}-${Math.random().toString(16).slice(2)}`;
  return {
    all(){return read()},
    saveSession(data){const db=read();const session={id:uid(),createdAt:new Date().toISOString(),reviewed:false,...data};db.sessions.unshift(session);write(db);return session},
    update(id,patch){const db=read();const i=db.sessions.findIndex(x=>x.id===id);if(i>=0){db.sessions[i]={...db.sessions[i],...patch};write(db)}},
    replace(data){if(!data||!Array.isArray(data.sessions))throw new Error('档案格式不正确');write({...empty(),...data,version:1})},
    clear(){write(empty())}
  }
})();
