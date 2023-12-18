const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs'); 

async function scrapeHtmlTags(url) {
    try {
        // Make a GET request to the URL
        const response = await axios.get(url);
        const html = response.data;

        // Parse the HTML content
        const $ = cheerio.load(html);

        // Find all <a> tags
        const links = [];
        $('a').each((index, element) => {
            const href = $(element).attr('href');
            if (href != undefined)
            {
                if(!href.startsWith('/list/')){
                    links.push(encodeURI('https://areq.net'+ href));
                }
            }
        });
        fs.writeFileSync ('urls.txt', links.join('\n'));

    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

// with the URL you want to scrape
scrapeHtmlTags('https://areq.net/mw/%D9%85%D9%88%D8%B3%D9%88%D8%B9%D8%A9_%D8%B9%D9%84%D9%85_%D8%A7%D9%84%D8%A8%D9%8A%D8%A6%D8%A9.html');
