# Simulação de protocolos de transmissão de rede

Protocolo Aloha: O Protocolo Aloha é um dos primeiros protocolos de acesso ao meio usados em redes de computadores. Ele foi desenvolvido na Universidade do Havaí no final dos anos 1960. O Protocolo Aloha é um protocolo de acesso múltiplo não controlado, o que significa que os dispositivos em uma rede podem transmitir dados a qualquer momento, sem coordenar com outros dispositivos. Se houver colisões de dados (ou seja, dois dispositivos transmitindo ao mesmo tempo), eles são detectados, e os dispositivos tentam novamente após um período de espera aleatório. Existem variações do Protocolo Aloha, como o Aloha Puro e o Slotted Aloha, que introduzem melhorias na eficiência do protocolo.

P-persistence: O P-persistence é um conceito que se aplica aos protocolos de acesso ao meio, como o CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance), que é frequentemente usado em redes sem fio, como o Wi-Fi. No contexto do P-persistence, um dispositivo que deseja transmitir dados "ouvirá" o meio para verificar se ele está ocupado. Se o meio estiver ocupado, o dispositivo espera até que o meio esteja livre. O valor "P" no P-persistence representa uma probabilidade de transmissão. Em vez de simplesmente esperar, o dispositivo pode usar uma probabilidade (P) para determinar quando deve tentar transmitir. Por exemplo, se P for definido como 0,5 (50%), o dispositivo terá uma chance de 50% de tentar transmitir quando o meio estiver livre. Isso ajuda a evitar colisões frequentes e aumenta a eficiência do acesso ao meio.

Recuo binário (Binary Exponential Backoff): O recuo binário é um algoritmo usado em protocolos de acesso ao meio, especialmente em Ethernet, para lidar com colisões. Quando ocorre uma colisão de dados (ou seja, dois dispositivos tentam transmitir ao mesmo tempo), os dispositivos envolvidos usam o algoritmo de recuo binário para determinar quando tentar novamente. O dispositivo espera por um período de tempo aleatório e depois tenta novamente. Se outra colisão ocorrer, ele aumenta o período de espera exponencialmente (dobra o tempo de espera) e tenta novamente. Esse processo de aumento exponencial continua até que a tentativa de transmissão seja bem-sucedida. O recuo binário ajuda a reduzir a probabilidade de colisões repetidas e melhora o desempenho da rede.
