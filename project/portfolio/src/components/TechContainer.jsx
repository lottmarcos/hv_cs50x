import '../styles/components/techcontainer.sass'

const technologies = [
  {id: "html", name: "HTML5", icon: "../../public/html-icon.png", text: " HTML is the standard markup language for documents designed to be displayed in a web browser."},
  {id: "css", name: "CSS3", icon: "../../public/css-icon.png", text: "CSS is a style sheet language used for describing the presentation of a document written in a markup language."},
  {id: "js", name: "JavaScript", icon: "../../public/js-icon.png", text: "JavaScript is a programming language that is one of the core technologies of the World Wide Web."},
  {id: "react", name: "React", icon: "../../public/react-icon.png", text: "React is a open-source front-end JavaScript library for building user interfaces based on UI components."},
  {id: "python", name: "Python", icon: "../../public/python-icon.png", text: "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."},
  {id: "cpp", name: "C++", icon: "../../public/cpp-icon.png", text: "C++ is a cross-platform programming language that can be used to create high-performance applications."},
]

const TechContainer = () => {
  return (
    <section className='tech-container'>
      <h2>technologies</h2>
      <div className='tech-grid'>
        {technologies.map((tech) => (
          <div className="tech-card" id={tech.id} key={tech.id}>
            <img src={tech.icon} />
            <div className='tech-info'>
              <h3>{tech.name}</h3>
              <p>{tech.text}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}

export default TechContainer  