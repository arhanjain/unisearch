import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

import { API, Auth } from 'aws-amplify'
import '@aws-amplify/ui-react/styles.css';
import Search from './components/Search'

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
      {/* <Authenticator>
        {({ signOut, user}) => ( */}
          <div className=' h-screen w-full'>
            <div className='h-full flex justify-evenly items-center'>
              <Search classNames={"w-1/2"}/>
            </div>
            {/* <button onClick={signOut}>Sign Out</button> */}

          </div>
        {/* )}
      </Authenticator> */}
    </>
  )
}

export default App
