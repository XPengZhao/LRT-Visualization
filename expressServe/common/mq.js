var amqp = require('amqplib/callback_api');

class RabbitMQ{

    create(data){
        amqp.connect('amqp://admin:admin@158.132.255.123:5672', function(error0, connection) {
            if (error0) {
                throw error0;
            }
            connection.createChannel(function(error1, channel) {
                if (error1) {
                    throw error1;
                }

                var queue = 'replay';

                channel.assertQueue(queue, {
                    durable: true
                });
                for(let i = 0;i<data.length;i++){
                    setTimeout(function (){
                        let msg={
                            tagId:data[i].tagId,
                            logTime:data[i].logTime,
                            phyTime:data[i].phyTime,
                            savedTime:data[i].savedTime,
                            position: data[i].position,
                            truth:data[i].truth,
                            xServer: data[i].xServer,
                            spectrum:data[i].spectrum,
                            end: i===data.length-1
                        }
                        channel.sendToQueue(queue,Buffer.from(JSON.stringify(msg)))
                    },(i+1)*10)

                }

            })


    })
    }
}

module.exports = new RabbitMQ()
