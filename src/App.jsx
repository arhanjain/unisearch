import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

import { API, Auth } from 'aws-amplify'
import { Authenticator, useAuthenticator, withAuthenticator } from '@aws-amplify/ui-react'
import '@aws-amplify/ui-react/styles.css';

function App() {

  async function testAPI() {
    const user = await Auth.currentAuthenticatedUser()
    const token = user.signInUserSession.idToken.jwtToken
    console.log({token})
    const params = {
      headers: {
        Authorization: token
      },
      body: {
        papers: ["www.github.com", "www.google.com"]
      }
    }

    API.post('unisearchAPI', '/add-papers', params)
      .then(data => {
        console.log(data)
      })
    }

  return (
    <>
      <Authenticator>
        {({ signOut, user}) => (
          <>
            <div>
              <a href="https://vitejs.dev" target="_blank">
                <img src={viteLogo} className="logo" alt="Vite logo" />
              </a>
              <a href="https://react.dev" target="_blank">
                <img src={reactLogo} className="logo react" alt="React logo" />
              </a>
            </div>
            <h1>Sup, {user.attributes.email}</h1>
            <button onClick={testAPI}>HELLOOO</button>
            <button onClick={signOut}>Sign Out</button>

          </>
        )}
      </Authenticator>
    </>
  )
}

export default App
