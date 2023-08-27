import React, { Children } from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

import { 
  createBrowserRouter,
  RouterProvider
 } from 'react-router-dom'

import {Authenticator} from '@aws-amplify/ui-react'
import { Amplify } from 'aws-amplify'
import awsExports from './aws-exports'
import Root from './components/Root.jsx'
Amplify.configure(awsExports)

const router = createBrowserRouter([
  {
    path: '/',
    element:<Root/> ,
    children: [
      { 
        path: '/',
        element: <App/> 
      },
      // {
      //   path: '/mypapers',
      // }
    ]    
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Authenticator.Provider>
      <RouterProvider router={router}/>
    </Authenticator.Provider>
  </React.StrictMode>,
)
