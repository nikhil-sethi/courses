function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);
##J_history=10
tol= 10e-3;
for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCostMulti) and gradient here.
    %

    grad = mean((X*theta-y).*X)';
    theta = theta - alpha * (grad);

    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCostMulti(X, y, theta);
##    del_J= J_history(iter-1)-J_history(iter)
##    if 0 < del_J < tol
##      fprintf("Optimisation terminated. Tolerance reached");
##      break;
##      
##    elseif del_J<0
##      fprintf("Wrong. J is increasing! Check your learning rate");
##      break;
##      
##    endif
    
end

end

