db = db.getSiblingDB('bank');

db.createUser({
  user: 'root',
  pwd: 'root',
  roles: [
    {
      role: 'root',
      db: 'bank',
    },
  ],
});