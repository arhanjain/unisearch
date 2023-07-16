import React, { Component, useCallback, useState } from 'react';
import axios from 'axios';
import {debounce} from 'lodash';
import xml2js from 'xml2js'
import SearchResultCard, {SearchResult} from './SearchResultCard';
import { string } from 'yargs';

type InputTypes = {
    classNames: string,
}

interface ArxivResults {
    title: string,
    author: Array<{name:Array<string>}>,
    link: Array<{$:{href:string}}>
}

const ARXIV_QUERY_API = 'http://export.arxiv.org/api/query'
function Search({classNames}: InputTypes) {
    const [articles, setArticles] = useState<Array<SearchResult>>([])
    const searchChange = (text: string) => {
            if (text.length == 0) {
                setArticles([]);
                return;
            }
            axios.get(ARXIV_QUERY_API,{params: {
                search_query: "all:"+text,
                start: 0,
                max_results: 5
            }}).then(res => {
                xml2js.parseString(res.data, (err, result) => {
                    console.log(result)
                    if (!result.feed.entry) setArticles([])
                    else{
                        setArticles(result.feed.entry.map((e: ArxivResults) => ({
                            title: e.title[0],
                            authors: e.author.map(a => a.name[0]),
                            link: e.link[0].$.href
                        })))
                    }
                });
            })
            // axios.get('/search-articles', {params: {query:text}}).then(res => {
            //     setArticles(res.data.results)
            // }) 
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
                className='shadow appearance-none border rounded 
                w-full py-2 px-3 text-gray-700 leading-tight 
                focus:outline-none focus:shadow-outline'
            ></input>
            {articles.map(article => {
                return(<SearchResultCard data={article}></SearchResultCard>)
            })}
        </div>
    );
}

export default Search;