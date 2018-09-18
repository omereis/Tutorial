let person = {
    name: 'Homer',
    age: 61,
    weekendAlarm: 'No alarms needed',
    weekAlarm : 'Alarm set to 7AM',
  //  `Hello, my name is ${name here}`
    sayHello: () => { return `Hello, my name is ${this.name}`;},
//    sayHello: () => { return `Hello, my name is ${this.name}`},
    sayGoodbye() {
      return 'Goodbye!'
    }
  };
  
  person.hobbies = ['Stamps Collection', 'Gardening'];
  
  console.log(person['name']);
  console.log(person['age']);
  console.log(person.hobbies);
  console.log(person.sayHello());
  
  person.hobbies = ['Stamps Collection'];
  
  let day = 'Thursday';
  let alarm;
  
  if (day === 'Saturday' || day === 'Sunday') {
    alarm = 'weekendAlarm';
  }
  else {
    alarm = 'weekAlarm';
  }
  
  console.log(person[alarm]);
  