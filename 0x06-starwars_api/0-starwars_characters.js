#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch movie details
function fetchMovieDetails(url) {
    return new Promise((resolve, reject) => {
        request({
            url: url,
            rejectUnauthorized: false // Ignore SSL certificate verification
        }, (error, response, body) => {
            if (error) {
                reject(error);
                return;
            }
            resolve(JSON.parse(body));
        });
    });
}

// Function to fetch character details
function fetchCharacterDetails(url) {
    return new Promise((resolve, reject) => {
        request({
            url: url,
            rejectUnauthorized: false // Ignore SSL certificate verification
        }, (error, response, body) => {
            if (error) {
                reject(error);
                return;
            }
            const character = JSON.parse(body);
            resolve(character.name);
        });
    });
}

// Main function
async function main() {
    try {
        const movie = await fetchMovieDetails(apiUrl);
        const characterUrls = movie.characters;

        for (const url of characterUrls) {
            const characterName = await fetchCharacterDetails(url);
            console.log(characterName);
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

main();
