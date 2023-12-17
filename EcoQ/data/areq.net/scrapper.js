const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const readline = require('readline');
const { join } = require('path');


async function scrape_text(url) {
    try {
        // Make a GET request to the URL
        const response = await axios.get(url);
        const html = response.data;

        // Parse the HTML content
        const $ = cheerio.load(html);

        const content = [];
        $('p').each((index, element) => {
            const text = $(element).text();
            if (text != undefined && !/^[a-zA-Z]+$/.test(text))
            {  
                content.push(text)
            }
        });
        file_name = decodeURI(url).split('/')[4].split('.')[0] + '.txt';
        file_path = join(process.cwd(), 'scrapped_articles', file_name);
        fs.writeFileSync(file_path, content.join('\n\n'));


    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

// reading urls file line by line
const readInterface = readline.createInterface({
    input: fs.createReadStream('urls.txt'),
});

readInterface.on('line', function(line) {
    scrape_text(line);
});



// const axios = require('axios');
// const cheerio = require('cheerio');
// const fs = require('fs');
// const readline = require('readline');

// async function scrape_text(url) {
//     try {
//         // Make a GET request to the URL
//         const response = await axios.get(url);
//         const html = response.data;

//         // Parse the HTML content
//         const $ = cheerio.load(html);

//         const content = [];
//         $('p').each((index, element) => {
//             const text = $(element).text();
//             if (text != undefined && /^[a-zA-Z]+$/.test(text))
//             {  
//                 content.push(text)
//             }
//         });
        
//         fs.appendFile('scraping.txt', content.join('\n'), function (err) {
//             if (err) throw err;
//         });
        


//     } catch (error) {
//         console.error(`Error: ${error.message}`);
//     }
// }

// // reading urls file line by line
// const readInterface = readline.createInterface({
//     input: fs.createReadStream('urls.txt'),
// });

// readInterface.on('line', function(line) {
//     scrape_text(line);
// });


// npm i axios cheerio 