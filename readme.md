# Leaning Note
## Layers

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
 