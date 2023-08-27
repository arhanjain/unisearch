import React, { Component, useCallback, useState } from 'react';
import axios from 'axios';
import {debounce} from 'lodash';
import SearchResultCard from './SearchResultCard';

const ARXIV_QUERY_API = 'https://export.arxiv.org/api/query'
function Search({classNames}) {
    const [articles, setArticles] = useState([])
    const domParser = new DOMParser();
    const searchChange = (text) => {
            if (text.length == 0) {
                setArticles([]);
                return;
            }
            axios.get(ARXIV_QUERY_API,{params: {
                search_query: "all:"+text,
                start: 0,
                max_results: 5
            }}).then(res => {
                const parsed = domParser.parseFromString(res.data, "text/xml")
                console.log(parsed)
                // check if there are any entrys in the xml
                if (!parsed.getElementsByTagName("entry")) setArticles([])
                else{
                    setArticles(Array.from(parsed.getElementsByTagName("entry")).map((e) => ({
                        title: e.getElementsByTagName("title")[0].innerHTML,
                        authors: Array.from(e.getElementsByTagName("author")).map(a => a.getElementsByTagName("name")[0].innerHTML),
                        link: e.getElementsByTagName("link")[0].getAttribute("href")
                    })))
                }
                // xml2js.parseString(res.data, (err, result) => {
                //     console.log(result)
                //     if (!result.feed.entry) setArticles([])
                //     else{
                //         setArticles(result.feed.entry.map((e) => ({
                //             title: e.title[0],
                //             authors: e.author.map(a => a.name[0]),
                //             link: e.link[0].$.href
                //         })))
                //     }
                // });
            })
    }

    const delayedSearch = useCallback(
        debounce(text => searchChange(text), 500),
        // (text:string) => searchChange(text),
        []
    )

    return (
        <div className={classNames}>
            <input 
                onChange={e => delayedSearch(e.target.value)}
                className='appearance-none border rounded-md h-16   
                w-full py-2 px-3 text-gray-700 border-black leading-tight border-2'
                placeholder="Search papers, notes, and people."
            ></input>
            {articles.map(article => {
                return(<SearchResultCard data={article}></SearchResultCard>)
            })}
        </div>
    );
}

export default Search;