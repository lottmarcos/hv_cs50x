import AboutContainer from './AboutContainer'
import TechContainer from './TechContainer'
import ProjectsContainer from './ProjectsContainer'

import '../styles/components/maincontent.sass'


const MainContent = () => {
   return (
      <main id="main-content">
         <AboutContainer />
         <TechContainer />
         <ProjectsContainer/>
      </main>
   )
}

export default MainContent