<div id="top"></div>

[![commits](https://badgen.net/github/commits/ChaserZ98/Fast-Trajectory-Replanning/main)](https://GitHub.com/ChaserZ98/Fast-Trajectory-Replanning/graphs/commit-activity)
[![forks](https://badgen.net/github/forks/ChaserZ98/Fast-Trajectory-Replanning)](https://GitHub.com/ChaserZ98/Fast-Trajectory-Replanning/network/members)
[![stars](https://badgen.net/github/stars/ChaserZ98/Fast-Trajectory-Replanning)](https://GitHub.com/ChaserZ98/Fast-Trajectory-Replanning/stargazers)
[![issues](https://badgen.net/github/issues/ChaserZ98/Fast-Trajectory-Replanning)](https://GitHub.com/ChaserZ98/Fast-Trajectory-Replanning/issues/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

<div align="center">
  <h1 align="center">Fast Trajectory Replanning</h1>
  <p align="center">
    A implementation of repeated A star algorithm.
    <br />
    <a href="https://GitHub.com/ChaserZ98/Fast-Trajectory-Replanning"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://GitHub.com/ChaserZ98/Fast-Trajectory-Replanning">View Demo</a>
    ·
    <a href="https://GitHub.com/ChaserZ98/Fast-Trajectory-Replanning/issues">Report Bug</a>
    ·
    <a href="https://GitHub.com/ChaserZ98/Fast-Trajectory-Replanning/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built with</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

This is a course project of Rutgers CS440 Intro to Artificial Intelligence.

### Built with

* Language:
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

* Python Packages:
  ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
  ![matplotlib version](https://img.shields.io/badge/matplotlib-3.5.0-brightgreen)


## License

Distributed under the MIT License.

See `LICENSE` for more information.

## Contact

Feiyu Zheng - [feiyuzheng98@gmail.com](mailto:feiyuzheng98@gmail.com)

Project Link: [https://github.com/ChaserZ98/Fast-Trajectory-Replanning](https://github.com/ChaserZ98/Fast-Trajectory-Replanning)

<p align="right">(<a href="#top">back to top</a>)</p>


## Part 1
(a) There are three available actions at E2, to the west, to the north and to the east. The destinations of three actions are respectively E1, D2 and E3.

`f(E1)=g(E1)+h(E1)=1+4=5`<br>
`f(D2)=g(D2)+h(D2)=1+4=5`<br>
`f(E3)=g(E3)+h(E3)=1+2=3`

Since E3 has the least f value, then the first move is to the E3, which is to the east.
