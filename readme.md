# Leaning Note
## Layers
### Entity
### Use Case
#### Interactor
#### Input Port
- Request Object
#### Output Port
- Response Object
### Interface Adaptrer
### External Interface
## Data Frow and Dependency
- [referenace](https://proandroiddev.com/clean-architecture-data-flow-dependency-rule-615ffdd79e29)
### DataFrom
1. Presenter/ViewModel.
    - UI  calls Method
2. Presenter/ViewModel
    - executes Use case.
3. Use case
    - combines data from User and Post Repositories.
4. Each Repository
    - returns data from a Data Source (Cached or Remote).
5. Information flows
    - back to the UI where we display the list of posts.

 ### Dependency Rule


 ## Component Cohesion
 - REP
 - CCP
 - CRP
 ### REP
 - classes and modules that are grouped together should be releasable together.
 - it should be make sense.
 - weak principle
 ### CCP
 - SRP restate for components.
 - chage should occur only in one component
