function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 0.3; #1
sigma = 0.1; #0.3

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%
#remove below code to optimize for C and sigma

##c_test=[0.01 0.1 0.3 0.9];
##s_test=[0.1 0.3 0.9 2.7];
##
##error_min=inf;
##for i=1:length(c_test)
##   for j=1:length(s_test)
##     #train svm with c_test and s_test
##     # predict output on CV set
##     # calc error
##     #print( error, c_test, s_test
##     curr_model = svmTrain(X ,y, c_test(i), @(x1, x2) gaussianKernel(x1, x2, s_test(j)));
##     pred = svmPredict(curr_model, Xval);
##     error = mean(double(pred~=yval));
##     if error<error_min
##       error_min = error;
##       C=c_test(i);
##       sigma=s_test(j);
##     endif
##     printf("cv error = %d, C = %d, sigma = %d",error, c_test(i), s_test(j));
##   endfor
##endfor
##
###printf("optimal C=%d", C); returned 0.3
###printf("optimal sigma=%d", sigma); returned 0.
##
##

% =========================================================================

end
