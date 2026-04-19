// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-welcome",
    title: "Welcome",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "publications",
          description: "Publications par catégories en ordre chronologique inversé.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/fr/publications/";
          },
        },{id: "nav-publications",
          title: "publications",
          description: "Publications by categories in reversed chronological order.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/en/publications/";
          },
        },{id: "nav-projets",
          title: "projets",
          description: "Projets de recherche, outils et initiatives communautaires à l&#39;intersection de la topologie, de la science des données et de l&#39;IA.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/fr/projects/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "Research projects, tools, and community initiatives at the intersection of topology, data science, and AI.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/en/projects/";
          },
        },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-livres",
          title: "livres",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/fr/books/";
          },
        },{id: "nav-bookshelf",
          title: "bookshelf",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/en/books/";
          },
        },{id: "nav-enseignement",
          title: "enseignement",
          description: "Cours de mathématiques pures, mathématiques appliquées, science des données et apprentissage automatique aux niveaux licence et master/doctorat.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/fr/teaching/";
          },
        },{id: "nav-teaching",
          title: "teaching",
          description: "Courses in pure mathematics, applied mathematics, data science, and machine learning at undergraduate and graduate levels.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/en/teaching/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "CV académique du Dr. Yaé Ulrich Gaba — formation, expérience, compétences et publications.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/fr/cv/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "Academic CV of Dr. Yaé Ulrich Gaba — education, experience, skills, and publications.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/en/cv/";
          },
        },{id: "nav-repositories",
          title: "repositories",
          description: "Open-source tools, research code, and teaching materials.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-conseil",
          title: "conseil",
          description: "Services de conseil en IA et science des données — stratégie, ateliers et recherche appliquée.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/fr/consulting/";
          },
        },{id: "nav-consulting",
          title: "consulting",
          description: "AI and data science consulting services — strategy, workshops, and applied research.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/en/consulting/";
          },
        },{id: "post-persistence-landscapes-as-ml-features-a-complete-pipeline",
        
          title: "Persistence landscapes as ML features: a complete pipeline",
        
        description: "A step-by-step guide to computing persistence landscapes and using them as features in machine learning pipelines.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/persistence-landscapes-ml-pipeline/";
          
        },
      },{id: "post-building-ai-research-labs-in-africa-lessons-from-airina-labs",
        
          title: "Building AI research labs in Africa: lessons from AIRINA Labs",
        
        description: "Reflections on founding and growing an AI research lab on the continent — what works, what&#39;s hard, and why it matters.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/building-ai-research-africa/";
          
        },
      },{id: "post-llms-meet-topology-can-tda-improve-language-model-interpretability",
        
          title: "LLMs meet topology: can TDA improve language model interpretability?",
        
        description: "Exploring how topological data analysis can shed light on the inner workings of large language models — from attention geometry to representation topology.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/llms-meet-topology/";
          
        },
      },{id: "post-announcing-the-shape-of-data",
        
          title: "Announcing: The Shape of Data",
        
        description: "Our book on geometry-based machine learning is now available from No Starch Press.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/shape-of-data-announcement/";
          
        },
      },{id: "post-the-african-ai-landscape-opportunities-and-challenges",
        
          title: "The African AI landscape: opportunities and challenges",
        
        description: "Reflections on building AI research capacity across Africa — from AIMS to Data Science Africa and beyond.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/african-ai-landscape/";
          
        },
      },{id: "post-getting-started-with-tda-in-python",
        
          title: "Getting started with TDA in Python",
        
        description: "A practical introduction to Topological Data Analysis using Python — from point clouds to persistence diagrams.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/tda-python-tutorial/";
          
        },
      },{id: "post-fixed-points-and-convergence-in-reinforcement-learning",
        
          title: "Fixed points and convergence in reinforcement learning",
        
        description: "How the Banach fixed point theorem explains why RL algorithms converge — bridging topology and decision-making.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/fixed-points-in-rl/";
          
        },
      },{id: "post-why-topology-matters-for-machine-learning",
        
          title: "Why topology matters for machine learning",
        
        description: "An introduction to how topological ideas are reshaping modern machine learning — from persistent homology to geometric deep learning.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/topology-for-machine-learning/";
          
        },
      },{id: "books-the-shape-of-data-geometry-based-machine-learning-and-data-analysis-in-r",
          title: 'The Shape of Data: Geometry-Based Machine Learning and Data Analysis in R',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_shape_of_data/";
            },},{id: "news-the-shape-of-data-our-book-on-geometry-based-machine-learning-and-data-analysis-in-r-is-now-available-from-no-starch-press-co-authored-with-colleen-m-farrelly",
          title: 'The Shape of Data — our book on geometry-based machine learning and data...',
          description: "",
          section: "News",},{id: "news-the-shape-of-data-notre-livre-sur-l-apprentissage-automatique-géométrique-et-l-analyse-de-données-en-r-est-disponible-chez-no-starch-press-co-écrit-avec-colleen-m-farrelly",
          title: 'The Shape of Data — notre livre sur l’apprentissage automatique géométrique et l’analyse...',
          description: "",
          section: "News",},{id: "news-new-preprint-topological-foundations-of-reinforcement-learning-is-now-available-on-arxiv-we-explore-how-algebraic-topology-illuminates-the-structure-of-rl-state-action-and-policy-spaces",
          title: 'New preprint: Topological Foundations of Reinforcement Learning is now available on arXiv. We...',
          description: "",
          section: "News",},{id: "news-nouveau-preprint-topological-foundations-of-reinforcement-learning-est-disponible-sur-arxiv-nous-explorons-comment-la-topologie-algébrique-éclaire-la-structure-des-espaces-d-états-d-actions-et-de-politiques-en-rl",
          title: 'Nouveau preprint : Topological Foundations of Reinforcement Learning est disponible sur arXiv. Nous...',
          description: "",
          section: "News",},{id: "news-joined-airina-labs-as-head-of-r-amp-amp-d-leading-research-at-the-intersection-of-topology-geometry-and-applied-ai",
          title: 'Joined AIRINA Labs as Head of R&amp;amp;amp;D, leading research at the intersection of...',
          description: "",
          section: "News",},{id: "news-arrivée-chez-airina-labs-en-tant-que-directeur-r-amp-amp-d-à-la-tête-de-la-recherche-à-l-intersection-de-la-topologie-la-géométrie-et-l-ia-appliquée",
          title: 'Arrivée chez AIRINA Labs en tant que Directeur R&amp;amp;amp;D, à la tête de...',
          description: "",
          section: "News",},{id: "news-new-preprint-bellman-operator-convergence-enhancements-in-reinforcement-learning-algorithms-is-now-on-arxiv-with-david-krame-kadurha-and-domini-jocema-leko-moutouo",
          title: 'New preprint: Bellman Operator Convergence Enhancements in Reinforcement Learning Algorithms is now on...',
          description: "",
          section: "News",},{id: "news-nouveau-preprint-bellman-operator-convergence-enhancements-in-reinforcement-learning-algorithms-est-sur-arxiv-avec-david-krame-kadurha-et-domini-jocema-leko-moutouo",
          title: 'Nouveau preprint : Bellman Operator Convergence Enhancements in Reinforcement Learning Algorithms est sur...',
          description: "",
          section: "News",},{id: "news-new-blog-post-llms-meet-topology-exploring-how-topological-data-analysis-can-improve-large-language-model-interpretability-read-it-here",
          title: 'New blog post: LLMs Meet Topology — exploring how topological data analysis can...',
          description: "",
          section: "News",},{id: "news-nouveau-billet-de-blog-llms-meet-topology-explorer-comment-l-analyse-topologique-des-données-peut-améliorer-l-interprétabilité-des-grands-modèles-de-langage-lire-ici",
          title: 'Nouveau billet de blog : LLMs Meet Topology — explorer comment l’analyse topologique...',
          description: "",
          section: "News",},{id: "projects-topological-foundations-of-reinforcement-learning",
          title: 'Topological foundations of reinforcement learning',
          description: "Applying algebraic topology to understand the structure of RL state, action, and policy spaces.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_topological_rl/";
            },},{id: "projects-the-shape-of-data",
          title: 'The Shape of Data',
          description: "Geometry-Based Machine Learning and Data Analysis in R — co-authored book published by No Starch Press.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_shape_of_data/";
            },},{id: "projects-wocomtoqc-workshop",
          title: 'WoComToQC Workshop',
          description: "Workshop on Computational Topology &amp; Quantum Computing — interdisciplinary research event.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_wocomtoqc/";
            },},{id: "projects-intelligent-resource-allocation-via-deep-rl",
          title: 'Intelligent resource allocation via deep RL',
          description: "Deep Q-Networks for wireless network resource allocation and optimization.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_dqn_wireless/";
            },},{id: "projects-ml-teaching-materials",
          title: 'ML teaching materials',
          description: "Open-source machine learning teaching materials and Jupyter notebooks for beginners.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_ml_teaching/";
            },},{id: "projects-geometric-ml-toolkit",
          title: 'Geometric ML toolkit',
          description: "Tools and notebooks for geometric and topological machine learning in R and Python.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_geometric_ml/";
            },},{id: "teachings-introduction-to-topological-data-analysis",
          title: 'Introduction to Topological Data Analysis',
          description: "A workshop-style course introducing the foundations of TDA — persistent homology, filtrations, and applications to data science. Designed for graduate students and researchers at AIMS and partner institutions.",
          section: "Teachings",handler: () => {
              window.location.href = "/teachings/data-science-fundamentals/";
            },},{id: "teachings-machine-learning-for-beginners",
          title: 'Machine learning for beginners',
          description: "An accessible introduction to machine learning concepts and Python tools, designed for African graduate students and early-career researchers.",
          section: "Teachings",handler: () => {
              window.location.href = "/teachings/introduction-to-machine-learning/";
            },},{
        id: 'social-cv',
        title: 'CV',
        section: 'Socials',
        handler: () => {
          window.open("/assets/pdf/cv_gaba.pdf", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%67%61%62%61%79%61%65%32@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=UTszjV4AAAAJ", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0000-0001-8128-9704", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/gabayae", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/gabayae", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
