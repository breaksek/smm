const axios = require('axios');

async function connect(end_point, post) {
    try {
        const headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'
        };
        const response = await axios.post(end_point, new URLSearchParams(post), { headers });
        return response.data;
    } catch (error) {
        console.error(error);
        return false;
    }
}

// Contoh membuat pesanan
api_url = 'api_url';
post_data = {
    api_key: 'randomkey',
    action: 'order',
    secret_key: 'secret_key',
    service: 1,
    data: 'nasa',
    quantity: 150
};
connect(api_url, post_data).then(api => console.log(api));
